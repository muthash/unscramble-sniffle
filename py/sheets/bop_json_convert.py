import random

para = ["A", "B", "C"]
ai = {
    "BUILDING_OWNER, LOSS": {
        "contractNumber": "ABC-CONTRACT-098",
        "buildingDescription": "the great building"
    },
    "LESSOR_OF_EQUIPMENT": {
        "descriptionOfLeasedEquipment": "Trucks",
    },
    "LOSS_PAYABLE": {
        "contractNumber": "ABC-CONTRACT-098",
        "buildingDescription": "the great building",
        "paragraph": random.choice(para)
    },
    "LOSS_OF_RENTAL_VALUE": {
        "designationOfPremises": "The loss of rental value manager",
        "limitOfInsurance": 200000
    },
    "MANAGER_OF_PREMISES": {
        "designationOfPremises": "This is the manager of premises"
    },
    "MORTGAGE_HOLDER": {
        "contractNumber": "ABC-CONTRACT-100",
    },    
    "OWNERS_COMPLETED_OPS": {
        "additionalInformation": "The owners additional completed operations"
    },
    "VENDORS": {
        "productDescription": "This are very nice products"
    }
}
business_name = ["Stephen Muthama Business", "Dave Mathews Business", "Hemal Patel Business"]
addresses = [
    {
        "addressLine1": "1139 Riverbend Dr",
        "city": "Bermuda Run",
        "state": "NC",
        "zipCode": "27006"
    },
    {
        "addressLine1": "201 Varick Street",
        "city": "New York",
        "state": "NY",
        "zipCode": "10014" 
    },
    {
        "addressLine1": "2993 Curtis Street",
        "city": "Des Plaines",
        "state": "IL",
        "zipCode": "60018"
    }
]
addressTypes = ["billing", "business", "home", "other"]
disabled = ["ENGINEERS", "ENGINEERS_NOT_ENGAGED", "GRANTOR_OF_FRANCHISE", "OWNERS",
        "STATE_SUBDIVISIONS_AUTHORIZATIONS", "STATE_SUBDIVISIONS"]
waiver = [{ "name": "Dave Mathews"}, { "name": "Hemal Patel"}]
vCount = ["privatePassengerVehicles", "lightTrucks", "mediumTrucks", "heavyTrucks", "shortHaulExtraHeavyTrucksAndTractors",
          "longHaulExtraHeavyTrucksAndTractors", "cementMixers", "busesOver20Passengers"]
vStates = {"Florida": "FL", "Louisiana": "LA", "New Hampshire": "NH", "Vermont": "VT", "West Virginia": "WV"}
pay = {"One-time": 1, "Four": 4, "Ten": 10}

company_name = ""

def insert_cell_value(sheet, data, cell, col):
    val = "" if cell.value is None else cell.value
    if val == "Yes" or val == "YES" or val == "yes":
        val = True
    elif val == "No" or val == "NO":
        val = False
    

    if col == 0: 
        data["loginCredentials"]["username"] = val
    elif col == 1: 
        data["loginCredentials"]["password"] = val
    elif col == 2: 
        global company_name 
        company_name = val
        data["featureSets"][0]["testData"]["companyName"] = val
        data["description"] = sheet.title + " - " + val
        data["featureSets"][0]["description"] = "Create ACCOUNT - " + val
        data["featureSets"][1]["description"] = "Quote BOP - " + val
    elif col == 3: 
        data["featureSets"][1]["testData"]["policyInfo"]["organizationType"] = val
    elif col == 4: data["featureSets"][0]["testData"]["NAICSCode"] = val
    elif col == 5: data["featureSets"][0]["testData"]["NAICSDescription"] = val
    elif col == 6: 
        data["featureSets"][0]["testData"]["address"]["addressLine1"] = val
    elif col == 7: 
        data["featureSets"][0]["testData"]["address"]["addressLine2"] = val
    elif col == 8: 
        data["featureSets"][0]["testData"]["address"]["city"] = val
    elif col == 9: 
        data["featureSets"][0]["testData"]["address"]["state"] = val
    elif col == 10: 
        data["featureSets"][0]["testData"]["address"]["zipcode"] = val
    elif col == 14: 
        data["featureSets"][1]["testData"]["policyInfo"]["yearsInBusiness"] = val
    elif col == 15: 
        data["featureSets"][1]["testData"]["locations"][0]["numberOfEmployees"] = val
    elif col == 16: 
        data["featureSets"][1]["testData"]["locations"][0]["AOPDeductible"] = val
    elif col == 17:
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["lessorsRisk"] = val
    elif col == 18: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["businessCategory"] = val
    elif col == 19: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["class"]["code"] = val
    elif col == 20: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"][ "class"]["descriptionCode"] = val
    elif col == 21: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["buildingLimit"] = val
    elif col == 22: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["businessPersonalPropertyLimit"] = val
    elif col == 23:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["contractorsPayroll"] = val
    elif col == 24:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["totalSales"] = val
    elif col == 25:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["alcoholSales"] = val
    elif col == 26: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["constructionType"] = val
    elif col == 27: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["numberOfStories"] = val
    elif col == 28: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["squareFootage"] = val
    elif col == 29: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["yearBuilt"] = val
    elif col == 30: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["roofUpdated"] = val
    elif col == 31: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["HVACUpdated"] = val
    elif col == 32: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["autoSprinklered"] = val
    elif col == 33:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["utilityServices"]["timeElement"] = val
    elif col == 34:
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["utilityServices"]["directDamage"] = val
    elif col == 35: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["BIEEPeriodOfIndemnity"] = val[0]
    elif col == 36: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["windCoverage"]["optIn"] = val
    elif col == 37: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["windCoverage"]["deductible"] = val
    elif col == 38: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["additionalBuildingCoverage"]["equipmentBreakdownCoverage"]["optIn"] = val
    elif col == 39: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["additionalBuildingCoverage"]["ordinanceOrLaw"]["optIn"] = val
    elif col == 40: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["additionalBuildingCoverage"]["ordinanceOrLaw"]["value"] = val
    elif col == 41:
         if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["additionalBuildingCoverage"]["spoilage"] = val
    elif col == 42:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["additionalBuildingCoverage"]["debrisRemoval"] = val
    elif col == 43: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["generalLiabilityPerOccurrence"] = val
    elif col == 44: 
        if val and val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["insuranceProduct"] = "XS"
            data["featureSets"][1]["description"] = "Quote XS - " + company_name
        # if not val:
        #     data["featureSets"][1]["testData"]["liabilityCoverages"]["excessLiabilityOptIn"] = val
    elif col == 45: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["medicalExpensesLiability"] = val
    elif col == 46: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["damageToPremises"] = val
    elif col == 47:
        data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["optIn"] = val
    elif col == 48: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["eachEmployeeLimit"] = val
    elif col == 49: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["aggregateLimit"] = val
        data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["retroactiveDate"] = {"numberOfDaysInFuture":0}
    elif col == 50: 
        data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["deductible"] = val
    elif col == 51:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["contractorsEachCoveredJobSite"] = val
    elif col == 52:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["propertyInTransit"] = val
    elif col == 53: 
        if val and val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["HNOA"] = {"optIn":val}
    elif col == 54:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["barberShops"] = {"optIn":val}
    elif col == 55:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["barberShops"]["numberOfOperators"] = val
    elif col == 56:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["beautySalons"] = {"optIn":val}
    elif col == 57:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["beautySalons"]["numberOfOperators"] = val
    elif col == 58:
        if val != "N/A":
            data["featureSets"][1]["testData"]["liabilityCoverages"]["snowPlowCoverage"] = {"optIn": val}

    elif col == 59: 
        data["featureSets"][1]["testData"]["additionalCoverages"]["employeeDishonestyLimit"] = val
    elif col == 60: 
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"] = {}
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["optIn"] = val
        if val and val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["retroactiveDate"] = {}
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["retroactiveDate"]["numberOfDaysInFuture"] = 0
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["eachEmploymentWrongfulActLimit"] = 100000
            data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["deductible"] = 10000
    elif col == 61:
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["terrorismCoverage"] = {"optIn": val}
    elif col == 62: 
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"] = {}
            data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"]["optIn"] = val
    elif col == 63: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"]["aggregateLimit"] = val
    elif col == 64: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"]["deductible"] = val
    elif col == 65: 
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["liquorLiability"] = {}
            data["featureSets"][1]["testData"]["additionalCoverages"]["liquorLiability"]["optIn"] = val
    elif col == 66: 
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["liquorLiability"]["eachCommonCauseLimit"] = val
    elif col == 67: 
        if val != 'N/A':
            data["featureSets"][1]["testData"]["additionalCoverages"]["liquorLiability"]["aggregateLimit"] = val
    elif col == 68:
        if val != "N/A":
            nval = val.split(', ')
            data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"] = []
            for index, ival in enumerate(nval):
                if ival not in disabled:
                    data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"].insert(0, dict())
                    data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"][0]["legalBusinessName"] = business_name[index]
                    data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"][0]["additionalInsuredType"] = ival
                    data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"][0]["addressType"] = addressTypes[index]
                    data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"][0]["address"] = addresses[index]
                    if ai.get(ival):
                        data["featureSets"][1]["testData"]["additionalCoverages"]["additionalInsureds"][0].update(ai[ival])
    elif col == 69:
        if val != "N/A":
            data["featureSets"][1]["testData"]["additionalCoverages"]["waiverOfSubrogation"] = []
            data["featureSets"][1]["testData"]["additionalCoverages"]["waiverOfSubrogation"].extend(waiver)
    # 70-waiversOfSubrogation - col 69
    elif col == 71:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"] = dict()
            data["featureSets"][1]["testData"]["excessLiability"]["limit"] = val     
    elif col == 72:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"] = dict()
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["optIn"] = val
    elif col == 73:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perAccidentLimit"] = val
    elif col == 74:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perDiseaseLimit"] = val
    elif col == 75:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perPolicyLimit"] = val
    elif col == 76:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"] = dict()
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["optIn"] = val
    elif col == 77:
        if val != "N/A":
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["combinedSingleLimit"] = val
    elif col == 78:
        if val != "N/A" and val != 'n/a':
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["vehicleCount"] = dict()
            nval = val.rstrip(",  ").split(",")
            for index, ival in enumerate(nval):
                 data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["vehicleCount"][vCount[index]] = ival.lstrip()
    # 79-excessCommercialAutoFleet - no data available
    elif col == 80:
        if val != "N/A" and val != 'n/a':
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["statesVisited"] = dict()
            nval = val.split(",")
            for ival in nval:
                if ival.strip() in vStates:
                    data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["statesVisited"][vStates[ival.strip()]] = True
    elif col == 82:
        data["featureSets"][1]["testData"]["expectedStatus"] = val.lower()
    elif col == 83:
        if val:
            data["featureSets"].append({})
            data["featureSets"][2]["description"] = "Bind BOP - " + company_name
            data["featureSets"][2]["type"] = "BIND"
            data["featureSets"][2]["execute"] = val
            data["featureSets"][2]["testData"] = {}
            data["featureSets"][2]["testData"]["context"] = "populate"
            data["featureSets"][2]["testData"]["shouldMatch"] = False
            data["featureSets"][2]["testData"]["insuranceProduct"] = "BOP"
            data["featureSets"][2]["testData"]["policyDetails"] = {"effectiveDate": {"numberOfDaysInFuture": 10}}
            data["featureSets"][2]["testData"]["policyDetails"][ "phoneNumber"] = "6092294392"
            data["featureSets"][2]["testData"]["policyDetails"]["insuredEmail"] = "davenmathews@gmail.com"
            data["featureSets"][2]["testData"]["policyDetails"]["secondaryInsuredEmail"] = "davenmathews+sec@gmail.com"
            data["featureSets"][2]["testData"]["expectedStatus"] = "in-force"
    elif col == 86:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["policyDetails"]["effectiveDate"]["numberOfDaysInFuture"] = val
    elif col == 87:
        if val and val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"] = {}
            data["featureSets"][2]["testData"]["insuranceProduct"] = "XS"
            data["featureSets"][2]["description"] = "Bind XS - " + company_name
    elif col == 89:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"]["carrierName"] = val
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"]["effectiveDate"] = {"numberOfDaysInFuture": 0}
    elif col == 92:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"]["carrierName"] = val
    elif col == 94:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"]["effectiveDate"] = {"numberOfDaysInFuture": 0 }
    elif col == 97:
        if val != "N/A" and val != "n/a":
            nval = val.split()
            ival = pay[nval[0]]
            data["featureSets"][2]["testData"]["paymentDetails"] = { "numberOfPayments": ival}
        # if sheet.title == "Multiclass":
        #     print(data["featureSets"][2])
