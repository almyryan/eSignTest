import json
data = '{"count":6,"results":[{"status":"DRAFT","description":"","language":"en","roles":[{"id":"CdUSIVjydnMC","emailMessage":{"content":""},"reassign":false,"locked":false,"specialTypes":[],"attachmentRequirements":[],"data":null,"type":"SENDER","index":0,"signers":[{"group":null,"language":"en","signature":null,"id":"7mlhKedQYysO","external":null,"delivery":{"provider":false,"download":true,"email":true},"updated":"2018-11-05T14:58:37Z","knowledgeBasedAuthentication":null,"professionalIdentityFields":[],"signerType":"ACCOUNT_SENDER","auth":{"scheme":"NONE","challenges":[]},"data":null,"firstName":"Ryan","lastName":"Almy","email":"ryan.s.almy@outlook.com","phone":"","company":"BHGE","userCustomFields":[],"title":null,"address":null,"created":"2018-11-05T00:00:00Z","name":"","specialTypes":[],"timezoneId":""}],"name":"Owner"},{"id":"Signer1","emailMessage":{"content":""},"reassign":false,"locked":false,"specialTypes":[],"attachmentRequirements":[],"data":null,"type":"SIGNER","index":0,"signers":[{"group":null,"language":"en","signature":null,"id":"Signer1","external":null,"delivery":{"provider":false,"download":false,"email":false},"updated":"2018-11-05T14:58:37Z","knowledgeBasedAuthentication":null,"professionalIdentityFields":[],"signerType":"EXTERNAL_SIGNER","auth":{"scheme":"NONE","challenges":[]},"data":null,"firstName":"John","lastName":"Smith","email":"signer@example.com","phone":"","company":"","userCustomFields":[],"title":"","address":null,"created":"2018-11-05T00:00:00Z","name":"","specialTypes":[],"timezoneId":""}],"name":"Signer1"}],"id":"kaHS0MFsVdIslYJOF9GSQ_brefI=","sender":{"status":"ACTIVE","language":"en","signature":null,"id":"7mlhKedQYysO","account":null,"external":null,"updated":"2018-09-10T22:03:48Z","locked":null,"professionalIdentityFields":[],"activated":null,"memberships":[],"data":{"serviceCredentials":"{}","showIntro":false},"firstName":"Ryan","lastName":"Almy","email":"ryan.s.almy@outlook.com","phone":"+12813805748","company":"BHGE","userCustomFields":[],"title":null,"type":"MANAGER","address":null,"created":"2018-09-10T22:03:49Z","name":"","specialTypes":[],"timezoneId":"GMT","hasDelegates":false},"documents":[{"status":"","description":"Must be accepted and agreed to before starting the signing process.","id":"default-consent","approvals":[],"external":null,"extract":false,"extractionTypes":[],"tagged":false,"signedHash":null,"signerVerificationToken":null,"pages":[{"id":"default-consent_0_-1_1.png","width":796.0,"height":1030.0,"left":0.0,"top":0.0,"version":0,"index":0},{"id":"default-consent_0_-1_2.png","width":796.0,"height":1030.0,"left":0.0,"top":0.0,"version":0,"index":1}],"data":{},"fields":[],"index":0,"name":"Electronic Disclosures and Signatures Consent","size":0},{"status":"","description":"","id":"sample-contract","approvals":[{"id":"ExampleSignatureId","role":"Signer1","optional":false,"accepted":null,"enforceCaptureSignature":false,"signed":null,"data":null,"fields":[{"binding":null,"validation":null,"id":"myLabelField","page":0,"subtype":"LABEL","extractAnchor":null,"extract":false,"width":198.89999270439148,"height":49.3999981880188,"left":98.7999963760376,"top":198.89999270439148,"data":null,"type":"INPUT","value":"Example label field value","name":""},{"binding":null,"validation":null,"id":"Ae8tTwET32s3","page":0,"subtype":"FULLNAME","extractAnchor":null,"extract":false,"width":199.99979266405106,"height":49.999948166012764,"left":100.00002633202077,"top":100.00002633202077,"data":null,"type":"SIGNATURE","value":"","name":"ExampleSignatureId"}],"name":""}],"external":null,"extract":false,"extractionTypes":[],"tagged":false,"signedHash":null,"signerVerificationToken":null,"pages":[{"id":"sample-contract_0_-1_1.png","width":774.0,"height":1095.0,"left":0.0,"top":0.0,"version":0,"index":0}],"data":{},"fields":[],"index":1,"name":"Test Document","size":13264}],"trashed":false,"consent":"default-consent","settings":{"ceremony":{"layout":{"header":{"globalActions":{"download":true,"confirm":true,"saveAsLayout":true,"hideEvidenceSummary":false},"globalNavigation":true,"sessionBar":true,"titleBar":{"title":true,"progressBar":true},"breadcrumbs":true,"feedback":true},"brandingBar":null,"footer":null,"iframe":false,"navigator":true},"inPerson":false,"enforceCaptureSignature":false,"handOver":null,"declineButton":true,"declineReasons":[],"disableDeclineOther":false,"disableDownloadForUncompletedPackage":false,"disableFirstInPersonAffidavit":false,"disableInPersonAffidavit":false,"disableOptOutOther":false,"disableSecondInPersonAffidavit":false,"documentToolbarOptions":null,"events":{"complete":{"redirect":null,"dialog":true}},"hideCaptureText":false,"hideLanguageDropdown":false,"hidePackageOwnerInPerson":false,"hideWatermark":false,"maxAuthFailsAllowed":3,"optOutButton":true,"optOutReasons":[],"extractAcroFields":false,"extractTextTags":false,"ada":false,"style":null}},"updated":"2018-11-05T14:58:38Z","due":null,"notarized":false,"notaryRoleId":null,"emailMessage":"","completed":null,"limits":null,"signedDocumentDelivery":null,"visibility":"ACCOUNT","data":{"origin":"api","currentSignerProgress":{"documentsToConfirmCount":"0","documentsConfirmedCount":"0","approvalsToConfirmCount":"0","approvalsConfirmedCount":"0","documentsPartiallyCompletedCount":"0","approvalsToSignNowCount":"0"},"overallProgress":{"documentsToCompleteCount":"2","documentsCompletedCount":"1","documentsToConfirmCount":"1","documentsConfirmedCount":"0","documentsPartiallyCompletedCount":"0"}},"autocomplete":true,"type":"PACKAGE","timezone":"GMT","messages":[],"created":"2018-11-05T14:58:38Z","name":"Example Package","bulkSendable":false}]}'
jsonToPython = json.loads(data)
print jsonToPython['count']