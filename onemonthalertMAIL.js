const fs = require('fs');
const csv = require('csv-parser');
const nodemailer = require('nodemailer');
const cron = require('node-cron');

let transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false,
    auth: {
        user: 'aviationlankaa@gmail.com',
        pass: 'hnhbecrmnzaphhjr'
    }
});

let lastRow = null;

fs.createReadStream('merged_file.csv')
    .pipe(csv({ mapHeaders: ({ header }) => header.trim() }))
    .on('data', (row) => {
        lastRow = row;
    })
    .on('end', () => {
        // Calculate the date 30 days before the deadline
        let deadlineDate = new Date(lastRow['TDeadline']);
        deadlineDate.setDate(deadlineDate.getDate() - 30);

        // Construct the cron pattern for 30 days before the deadline
        let cronPattern = `${deadlineDate.getMinutes()} ${deadlineDate.getHours()} ${deadlineDate.getDate()} ${deadlineDate.getMonth() + 1} *`;

        // Schedule the email to be sent on the calculated date
        cron.schedule(
            cronPattern,
            () => {
                let mailOptions = {
                    from: 'aviationlankaa@gmail.com',
                    to: lastRow['Scanned Email'],
                    subject: 'Aviation QR Scan Alert',
                    text: `You have an upcoming due:\n\nTool ID: ${lastRow['TScanned ID']}\n\nTool Name: ${lastRow['TScanned Name']}\n\nTool Checkout: ${lastRow['TCheck Out']}\n\nTool Deadline: ${lastRow['TDeadline']}`
                };

                transporter.sendMail(mailOptions, (error, info) => {
                    if (error) {
                        console.log(`Error sending email to ${lastRow['Scanned Email']}: ${error}`);
                    } else {
                        console.log(`Email sent to ${lastRow['Scanned Email']}: ${info.response}`);
                    }
                });
            },
            {
                scheduled: true,
                timezone: 'Asia/Colombo'
            }
        );
    });
