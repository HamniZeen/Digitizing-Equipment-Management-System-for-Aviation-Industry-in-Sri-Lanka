const fs = require('fs');
const csv = require('csv-parser');
const nodemailer = require('nodemailer');

let transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false,
    auth: {
        user: 'aviationlankaa@gmail.com',
        pass: 'vdvqrpahaqecoeaq'
    }
});

let lastRow=null;

fs.createReadStream('merged_file.csv')
    .pipe(csv({ mapHeaders: ({ header }) => header.trim() })) // trim headers to avoid whitespace issues
    .on('data', (row) => {
        lastRow=row;
    })
    .on('end', () => {
        let mailOptions = {
            from: 'aviationlankaa@gmail.com',
            to: lastRow['Scanned Email'],
            subject: 'Aviation QR Scan Alert',
            text: `This is to inform your Scanned Details; \n\n Employee ID: ${lastRow['Scanned EID']}\n\n Employee Name: ${lastRow['Scanned EName']}\n\n Tool ID: ${lastRow['TScanned ID']}\n\n Tool Name: ${lastRow['TScanned Name']}\n\n Tool Checkout: ${lastRow['TCheck Out']}\n\n Tool Deadline: ${lastRow['TDeadline']}`
        };
        
        transporter.sendMail(mailOptions, (error, info) => {
            if (error) {
                console.log(`Error sending email to ${lastRow['Scanned Email']}: ${error}`);
            } else {
                console.log(`Email sent to ${lastRow['Scanned Email']}: ${info.response}`);
            }
        });
    });
