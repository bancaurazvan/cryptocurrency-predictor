const sdk = require('./src/main.js');
sdkConfigure = sdk.configure({
    configSDK: {
        "evaluatorSDK": true,
        "evaluatorSDKPath": "/sdk/",
        "evaluatorSDKRootPath": "/sdk/"
    },
    evaluateSDK: {},
    rocketName: {
        "name": "n/a",
        "components": {
            "software": {},
            "hardware": {}
        }
    },
    appSupport: {
        // DO NOT EDIT THIS SECTION(APPSUPPORT), AS THIS IS AUTO-GENERATED!
        // appSupport Version 0.2.3
        "version": 0,
        "lastUpdated": "06232019",
        "system": "OSX",
        "systemVersion": "10.15.1",
        "systemArch": {
            "archName": "osx_darwin",
            "archType": "[map\ndarwin\n/\n64\n/\nfalse\nreadonly\nwriteonly\n]"
            /**
             * [map]
             */
        }
        // appSupport
    }
})
