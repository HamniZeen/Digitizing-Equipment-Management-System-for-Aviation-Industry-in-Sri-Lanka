const fs = require('fs');
const csv = require('csv-parser');
const nodemailer = require('nodemailer');

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

fs.createReadStream('Employee_Clean_ScannedData.csv')
    .pipe(csv({ mapHeaders: ({ header }) => header.trim() })) // trim headers to avoid whitespace issues
    .on('data', (row) => {
        lastRow = row;
    })
    .on('end', () => {
        let currentTime = new Date(); // Get the current date and time
        let formattedTime = currentTime.toLocaleString(); // Format the date and time as a string

        let mailOptions = {
            from: 'aviationlankaa@gmail.com',
            to: lastRow['Scanned Email'],
            subject: 'Aviation QR Scan Alert',
            text: `We just wanted to let you know that your QR Code is being Scanned at Aviation Lanka (Pvt) Ltd.\n\nEmployee ID: ${lastRow['Scanned EID']}\n\nEmployee Name: ${lastRow['Scanned EName']}\n\nOn ${formattedTime}`
        };

        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(`Error sending email to ${lastRow['Scanned Email']}: ${error}`);
            } else {
                console.log(`Email sent to ${lastRow['Scanned Email']}: ${info.response}`);
            }
        });
    });
