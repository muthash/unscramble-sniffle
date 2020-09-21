import random

para = ["A", "B", "C"]
ai = {
    "BUILDING_OWNER, LOSS": {
        "contractNumber": "ABC-CONTRACT-098",
        "buildingDescription": "the great building"
    },
    "LESSOR_OF_EQUIPMENT": {
        "additionalInformation": "Trucks",
    },
    "LOSS_PAYABLE": {
        "contractNumber": "ABC-CONTRACT-098",
        "buildingDescription": "the great building",
        "paragraph": random.choice(para)
    },
    "LOSS_OF_RENTAL_VALUE": {
        "additionalInformation": "The loss of rental value manager",
        "limitOfInsurance": 200000
    },
    "MANAGER_OF_PREMISES": {
        "additionalInformation": "This is the manager of premises"
    },
    "MORTGAGE_HOLDER": {
        "contractNumber": "ABC-CONTRACT-100",
    },    
    "OWNERS_COMPLETED_OPS": {
        "additionalInformation": "The owners additional completed operations"
    },
    "VENDORS": {
        "additionalInformation": "This are very nice products"
    }
}
business_name = ["Stephen Muthama Business", "Dave Mathews Business", "Hemal Patel Business"]
addresses = [
    {
        "addressLine1": "1139 Riverbend Dr",
        "city": "Bermuda Run",
        "state": "NC",
        "zip": "27006"
    },
    {
        "addressLine1": "201 Varick Street",
        "city": "New York",
        "state": "NY",
        "zip": "10014" 
    },
    {
        "addressLine1": "2993 Curtis Street",
        "city": "Des Plaines",
        "state": "IL",
        "zip": "60018"
    }
]
addressTypes = ["billing", "business", "home", "other"]
disabled = ["ENGINEERS", "ENGINEERS_NOT_ENGAGED", "GRANTOR_OF_FRANCHISE", "OWNERS",
        "STATE_SUBDIVISIONS_AUTHORIZATIONS", "STATE_SUBDIVISIONS"]
waiver = [{ "name": "Dave Mathews"}, { "name": "Hemal Patel"}]
vCount = ["privatePassengerVehicles", "lightTrucks", "mediumTrucks", "heavyTrucks", "shortHaulExtraHeavyTrucksAndTractors",
          "longHaulExtraHeavyTrucksAndTractors", "cementMixers", "busesOver20Passengers"]
vStates = {"Florida": "FL", "Louisiana": "LA", "New Hampshire": "NH", "Vermont": "VT", "West Virginia": "WV"}
pay = {"One-time": "ONE_PAY", "Four": "FOUR_PAY", "Ten": "TEN_PAY"}

company_name = ""

def find_coverage(name, coverages, updates):
    for val in coverages:
        if val['name'] == name:
            val['value'].update(updates)
            return True
    return False

def insert_cell_value(sheet, data, cell, col):
    val = "" if cell.value is None else cell.value
    if val == "Yes" or val == "YES" or val == "yes":
        val = True
    elif val == "No" or val == "NO" or val == "no":
        val = False
    

    # if col == 0: 
    #     data["loginCredentials"]["username"] = val
    # elif col == 1: 
    #     data["loginCredentials"]["password"] = val
    if col == 2: 
        global company_name 
        company_name = val
        data["featureSets"][0]["testData"]["name"] = val
        data["description"] = sheet.title + " - " + val
        data["featureSets"][0]["description"] = "Create ACCOUNT - " + val
        data["featureSets"][1]["description"] = "Quote BOP - " + val
    elif col == 3: 
        data["featureSets"][0]["testData"]["organizationType"] = val.lower()
    elif col == 4: data["featureSets"][0]["testData"]["naicsCodes"][0]["code"] = val
    elif col == 5: data["featureSets"][0]["testData"]["naicsCodes"][0]["description"] = val
    elif col == 6: 
        data["featureSets"][0]["testData"]["address"]["addressLine1"] = val
    elif col == 7: 
        data["featureSets"][0]["testData"]["address"]["addressLine2"] = val
    elif col == 8: 
        data["featureSets"][0]["testData"]["address"]["city"] = val
    elif col == 9: 
        data["featureSets"][0]["testData"]["address"]["state"] = val
    elif col == 10: 
        data["featureSets"][0]["testData"]["address"]["zip"] = val
    elif col == 14: 
        data["featureSets"][0]["testData"]["yearsInBusiness"] = int(val)
    elif col == 15: 
        data["featureSets"][1]["testData"]["locations"][0]["employeeCount"] = int(val)
    elif col == 16: 
        data["featureSets"][1]["testData"]["locations"][0]["propertyDeductible"] = int(val)
    elif col == 17:
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["lessorsRisk"] = val
    elif col == 18: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["businessType"] = val
    elif col == 19: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["classification"]["code"] = val
    elif col == 20: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["classification"]["descriptionCode"] = val
    elif col == 21: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["buildingLimit"] = int(val)
    elif col == 22: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["limitForBusinessPersonalProperty"] = int(val)
    elif col == 23:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["payroll"] = int(val)
    elif col == 24:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["totalSales"] = int(val)
    elif col == 25:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["alcoholSales"] = int(val)
    elif col == 26: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["constructionType"] = val
    elif col == 27: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["storyCount"] = val
    elif col == 28: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["squareFootage"] = int(val)
    elif col == 29: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["yearBuilt"] = int(val)
    elif col == 30: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["roofUpdated"] = val if val != "N/A" else False
    elif col == 31: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["electricPlumbingHVACUpdated"] = val if val != "N/A" else False
    elif col == 32: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["exposure"]["hasAutomaticSprinklerSystem"] = val
    elif col == 33:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["utilityServicesTimeElement"] = int(val)
    elif col == 34:
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["utilityServicesDirectDamage"] = int(val)
    elif col == 35: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["businessIncomeAndExtraExpensesIndemnityInMonths"] = int(val[0]+val[1]) if val[2] else int(val[0])
    # elif col == 36: 
    #     if val != "N/A":
    #         data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["windCoverage"]["optIn"] = val
    elif col == 37: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["windCoverage"]["windDeductiblePercent"] = "NotApplicable" if val == "N/A" else val
    elif col == 38: 
        data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["equipmentBreakdownCoverage"] = val
    # elif col == 39: 
    #     data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["ordinanceAndLawCoverage"]["ordinanceOrLaw"]["optIn"] = val
    elif col == 40: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["ordinanceAndLawCoverage"] = int(val)
    elif col == 41:
         if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["spoilageCoverage"] = int(val)
    elif col == 42:
        if val != "N/A":
            data["featureSets"][1]["testData"]["locations"][0]["buildings"][0]["coverage"]["debrisRemoval"] = int(val)
    elif col == 43: 
        data["featureSets"][1]["testData"]["policy"]["coverages"][0]["value"]["occurrenceLimit"] = int(val)
    elif col == 44: 
        if val and val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["insuranceProduct"] = "XS"
            data["featureSets"][1]["description"] = "Quote XS - " + company_name
        # if not val:
        #     data["featureSets"][1]["testData"]["liabilityCoverages"]["excessLiabilityOptIn"] = val
    elif col == 45: 
        data["featureSets"][1]["testData"]["policy"]["coverages"][1]["value"]["perPersonLimit"] = int(val)
    elif col == 46: 
        data["featureSets"][1]["testData"]["policy"]["coverages"][3]["value"]["occurrenceLimit"] = int(val)
    # elif col == 47:
    #     data["featureSets"][1]["testData"]["liabilityCoverages"]["EBLI"]["optIn"] = val
    elif col == 48:
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"][2]["value"]["perEmployeeLimit"] = int(val)
    elif col == 49:
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"][2]["value"]["aggregateLimit"] = int(val)
            data["featureSets"][1]["testData"]["policy"]["coverages"][2]["value"]["retroactiveDate"] = {"numberOfDaysInFuture":0}
    elif col == 50:
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"][2]["value"]["deductible"] = int(val)
    elif col == 51:
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                    "name": "Contractor",
                    "value": {
                        "perCoveredJobSiteLimit": int(val),
                    }
                })
    elif col == 52:
        if val != "N/A":
            name = "Contractor"
            updates = { "propertyInTransit": int(val)}
            coverages = data["featureSets"][1]["testData"]["policy"]["coverages"]
            result = find_coverage(name, coverages, updates)
            if not result:
                data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                    "name": "Contractor",
                    "value": {
                        "propertyInTransit": int(val),
                    }
                })
    elif col == 53: 
        if val and val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"][4]["value"]["optedIn"] = val
    # elif col == 54:
    #     if val != "N/A":
    #         data["featureSets"][1]["testData"]["liabilityCoverages"]["barberShops"] = {"optIn":val}
    elif col == 55:
        if val != "N/A":
             data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                    "name": "BarberShopsAndHairSalonsProfessionalLiability",
                    "value": {
                        "numOperators": int(val)
                    }
                })
    # elif col == 56:
    #     if val != "N/A":
    #         data["featureSets"][1]["testData"]["liabilityCoverages"]["beautySalons"] = {"optIn":val}
    elif col == 57:
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                    "name": "BeautySalonsProfessionalLiability",
                    "value": {
                        "numOperators": int(val)
                    }
                })
    elif col == 58:
        if val != "N/A":
             data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                    "name": "SnowPlowCompletedOps",
                    "value": {
                        "numOperators": int(val)
                    }
                })
    elif col == 59:
        data["featureSets"][1]["testData"]["policy"]["coverages"][5]["value"]["aggregateLimit"] = int(val)
    # elif col == 60: 
    #     if val != 'N/A':
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"] = {}
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["optIn"] = val
    #     if val and val != 'N/A':
    #         data["featureSets"][1]["testData"]["policy"]["coverages"][6]["value"]["aggregateLimit"] = val
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["eachEmploymentWrongfulActLimit"] = 100000
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["EPLI"]["deductible"] = 10000
    elif col == 61:
        if val != 'N/A':
            data["featureSets"][1]["testData"]["policy"]["coverages"].append(
                {
                "name": "CertifiedActsOfTerrorism",
                "value": {
                  "optedIn": val
                }
              },
            )
    # elif col == 62: 
    #     if val != 'N/A':
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"] = {}
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["cyberLiability"]["optIn"] = val
    elif col == 63: 
        if val != "N/A":
            data["featureSets"][1]["testData"]["policy"]["coverages"].append({
                "name": "CyberLiability",
                "value": {
                  "aggregateLimit": int(val),
                  "deductible": 1000,
                  "retroactiveDate": {
                    "numberOfDaysInFuture": 0
                  }
                }
              })
    elif col == 64: 
        if val != "N/A":
            name = "CyberLiability"
            updates = { "deductible": int(val),}
            coverages = data["featureSets"][1]["testData"]["policy"]["coverages"]
            result = find_coverage(name, coverages, updates)
            if not find_coverage(name, coverages, updates):
                print("CyberLiability " + result)
    # elif col == 65: 
    #     if val != 'N/A':
    #         data["featureSets"][1]["testData"]["policy"]["coverages"].append(
    #             {
    #             "name": "LiquorLiability",
    #             "value": {
    #               "aggregateLimit": 2000000,
    #               "perCommonCauseLimit": 1000000
    #             }
    #           }
    #         )
    elif col == 66: 
        if val != 'N/A' and val != 'n/a':
            data["featureSets"][1]["testData"]["policy"]["coverages"].append(
                {
                "name": "LiquorLiability",
                "value": {
                  "aggregateLimit": int(val)*2,
                  "perCommonCauseLimit": int(val)
                }
              }
            )
    # elif col == 67: 
    #     if val != 'N/A' and val != 'n/a':
    #         name = "LiquorLiability"
    #         updates = { "aggregateLimit" : int(val)}
    #         coverages = data["featureSets"][1]["testData"]["policy"]["coverages"]
    #         result = find_coverage(name, coverages, updates)
    #         if not find_coverage(name, coverages, updates):
    #             print(sheet.title)
    #             print(result)
    #             print('\n')
    elif col == 68:
        if val != "N/A" and val != 'n/a':
            nval = val.split(', ')
            mval = []
            for ival in nval:
                if ',' in ival:
                    mval = val.split(',')
                    nval.remove(ival)
            if mval:
                nval.extend(mval)
            
            if nval:
                data["featureSets"][1]["testData"]["additionalInsuredBusinesses"] = []
                for index, ival in enumerate(mval):
                    if ival not in disabled:
                        data["featureSets"][1]["testData"]["additionalInsuredBusinesses"].insert(0, dict())
                        data["featureSets"][1]["testData"]["additionalInsuredBusinesses"][0]["businessName"] = business_name[index]
                        data["featureSets"][1]["testData"]["additionalInsuredBusinesses"][0]["type"] = ival
                        data["featureSets"][1]["testData"]["additionalInsuredBusinesses"][0]["addressType"] = addressTypes[index]
                        data["featureSets"][1]["testData"]["additionalInsuredBusinesses"][0]["address"] = addresses[index]
                        if ai.get(ival):
                            data["featureSets"][1]["testData"]["additionalInsuredBusinesses"][0].update(ai[ival])
            
            if not data["featureSets"][1]["testData"]["additionalInsuredBusinesses"]:
                del data["featureSets"][1]["testData"]["additionalInsuredBusinesses"]

    # elif col == 69:
    #     if val != "N/A":
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["waiverOfSubrogation"] = []
    #         data["featureSets"][1]["testData"]["additionalCoverages"]["waiverOfSubrogation"].extend(waiver)
    # 70-waiversOfSubrogation - col 69
    elif col == 71:
        if val != "N/A":
            if val != "n/a":
                data["featureSets"][1]["testData"]["excessLiability"] = dict()
                data["featureSets"][1]["testData"]["excessLiability"]["limit"] = int(val)
    elif col == 72:
        if val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"] = dict()
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["optIn"] = val
    elif col == 73:
        if val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perAccidentLimit"] = int(val)
    elif col == 74:
        if val != "N/A"and val != "n/a" :
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perDiseaseLimit"] = int(val)
    elif col == 75:
        if val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["excessLiability"]["employersLiability"]["perPolicyLimit"] = int(val)
    elif col == 76:
        if val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"] = dict()
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["optIn"] = val
    elif col == 77:
        if val != "N/A" and val != "n/a":
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["combinedSingleLimit"] = int(val)
    elif col == 78:
        if val != "N/A" and val != 'n/a':
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["vehicleCount"] = dict()
            nval = val.rstrip(",  ").split(",")
            for index, ival in enumerate(nval):
                 data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["vehicleCount"][vCount[index]] = int(ival.lstrip())
    # 79-excessCommercialAutoFleet - no data available
    elif col == 80:
        if val != "N/A" and val != 'n/a':
            data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["statesVisited"] = dict()
            nval = val.split(",")
            for ival in nval:
                if ival.strip() in vStates:
                    data["featureSets"][1]["testData"]["excessLiability"]["commercialAuto"]["statesVisited"][vStates[ival.strip()]] = True
    elif col == 82:
        data["featureSets"][1]["expect"]["status"] = val.lower()
    elif col == 83:
        if val:
            data["featureSets"].append({})
            data["featureSets"][2]["description"] = "Bind BOP - " + company_name
            data["featureSets"][2]["testCasetype"] = "BIND"
            data["featureSets"][2]["execute"] = val if val != "n/a" else False
            data["featureSets"][2]["testData"] = {}
            data["featureSets"][2]["context"] = "populate"
            # data["featureSets"][2]["testData"]["shouldMatch"] = False
            data["featureSets"][2]["testData"]["insuranceProduct"] = "BOP"
            data["featureSets"][2]["testData"]["policyDetails"] = {"effectiveDate": {"numberOfDaysInFuture": 10}}
            data["featureSets"][2]["testData"]["policyDetails"]["insuredPhone"] = "6092294392"
            data["featureSets"][2]["testData"]["policyDetails"]["insuredEmail"] = "davenmathews@gmail.com"
            data["featureSets"][2]["testData"]["policyDetails"]["secondaryInsuredEmail"] = "davenmathews+sec@gmail.com"
            data["featureSets"][2]["expect"] = {"status": "in-force"}
    elif col == 86:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["policyDetails"]["effectiveDate"]["numberOfDaysInFuture"] = int(val)
    elif col == 87:
        if val and val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["insuranceProduct"] = "XS"
            data["featureSets"][2]["description"] = "Bind XS - " + company_name
    elif col == 89:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"]["carrierName"] = val
            data["featureSets"][2]["testData"]["excessLiability"]["employersLiability"]["effectiveDate"] = {"numberOfDaysInFuture": 0}
    elif col == 92:
        if val != "N/A" and val != "n/a":
            if "excessLiability" not in data["featureSets"][2]["testData"]:
                data["featureSets"][2]["testData"]["excessLiability"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"] = {}
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"]["carrierName"] = val
    elif col == 94:
        if val != "N/A" and val != "n/a":
            data["featureSets"][2]["testData"]["excessLiability"]["commercialAuto"]["effectiveDate"] = {"numberOfDaysInFuture": 0 }
    elif col == 97:
        if val != "N/A" and val != "n/a":
            nval = val.split()
            ival = pay[nval[0]]
            data["featureSets"][2]["testData"]["paymentPlan"] = ival
        # if sheet.title == "Multiclass":
        #     print(data["featureSets"][2])
