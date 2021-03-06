'use strict';
var Alexa = require("alexa-sdk");
var request = require('request');
var APP_ID = "amzn1.ask.skill.6db7c9a9-2b63-419b-9099-e63ea8706571";

exports.handler = function(event, context) {
    var alexa = Alexa.handler(event, context);
    alexa.appId = APP_ID;
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var handlers = {
    'SymptomLoggerIntent': function () {
        this.emit('LogSymptom');
    },
    'LogSymptom': function () {
        var part = this.event.request.intent.slots.Part.value;
        var sensation = this.event.request.intent.slots.Sensation.value;
        var intensity = this.event.request.intent.slots.Intensity.value;
        this.attributes['location'] = part;
        this.attributes['pain_type'] = sensation;
        this.attributes['severity'] = intensity;
        this.attributes['user'] = 1;

        const self=this;
        request({
            headers: {
                "Content-Type": "application/json"
            },
            url: "https://nwhacks-api.herokuapp.com/api/symptom",
            method: "POST",
            json: true,
            body: this.attributes
        }, function (error, response, body){
            if (!error) {
                console.log("P: " + part + " S: " + sensation + " I: " + intensity);
                console.log("D: " + body);
                self.response.speak('Your symptom has been recorded thank you');
                self.emit(':responseReady');
            }
            console.log("R:" + JSON.stringify(response));
        });


    },
    'SessionEndedRequest' : function() {
        console.log('Session ended with reason: ' + this.event.request.reason);
    },
    'AMAZON.StopIntent' : function() {
        this.response.speak('Bye. Thanks for using MediPrep');
        this.emit(':responseReady');
    },
    'AMAZON.CancelIntent' : function() {
        this.response.speak('Bye. Thanks for using MediPrep');
        this.emit(':responseReady');
    },
    'Unhandled' : function() {
        this.response.speak("Sorry, I didn't get that.");
    }
};
