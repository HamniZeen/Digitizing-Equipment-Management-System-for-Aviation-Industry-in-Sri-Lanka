const nodemailer = require('nodemailer');
const speakeasy = require('speakeasy');
const fs = require('fs');


const secret = speakeasy.generateSecret({ length: 10 }).base32;


const otp = speakeasy.totp({ secret: secret, encoding: 'base32' });


fs.writeFileSync('otp.txt', otp);


const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'aviationlankaa@gmail.com',
        pass: 'vdvqrpahaqecoeaq'
    }
});

const message = {
    from: 'aviationlankaa@gmail.com',
    to: 'hamnizeen@gmail.com',
    subject: 'OTP Verification',
    text: `Your OTP is ${otp}. Please use this to verify your account.`
};


function verifyOTP(userEnteredOTP) {
    const verified = speakeasy.totp.verify({
        secret: secret,
        encoding: 'base32',
        token: userEnteredOTP,
        window: 2 
    });

    return verified;
}

transporter.sendMail(message, (err, info) => {
    if (err) {
        console.log(err);
    } else {
        console.log(`Email sent: ${info.response}`);

        

process.exit();

       
    }
});
