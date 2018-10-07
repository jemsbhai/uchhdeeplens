/**
 * This is a sample Lambda function that sends an SMS notification when your
 * AWS DeepLens device detects a hot dog.
 * 
 * Follow these steps to complete the configuration of your function:
 *
 * Update the phone number environment variable with your phone number.
 */

const AWS = require('aws-sdk');
var request = require("request");


/*
*   Be sure to add email and phone_number to the function's environment variables
*/
const email = process.env.email;
const phone_number = process.env.phone_number;
const SNS = new AWS.SNS({ apiVersion: '2010-03-31' });

exports.handler = (event, context, callback) => {
    console.log('Received event:', event);

    // publish message
    const params = {
        Message: 'Your AWS DeepLens device just identified a potential patient. Congratulations!',
        PhoneNumber: phone_number
    };
    if (event.label.includes("Patient")) {
        //SNS.publish(params, callback);

        var options = { method: 'GET',
          url: 'http://c106fa6e.ngrok.io/testendpoint',
          headers: 
           { 'Postman-Token': 'e23261f6-f4ed-44d1-8d73-cdf3ff451df9',
             'Cache-Control': 'no-cache' } };
        
        request(options, function (error, response, body) {
          if (error) throw new Error(error);
        
          //console.log(body);
        });
    }
};