"""
This module contains default values for various Server API entities
"""


class TestCaseDefaults:
    CASE_FIELDS = ("id,projectId,archived,key,name,objective,majorVersion,latestVersion,"
                   "precondition,folder(id,fullName),status,priority,estimatedTime,"
                   "averageTime,componentId,owner,labels,customFieldValues,testScript(id,text,"
                   "steps(index,description,text,expectedResult,testData,attachments,"
                   "customFieldValues,id,stepParameters(id,testCaseParameterId,value),testCase("
                   "id,key,name,archived,majorVersion,latestVersion,parameters(id,name,"
                   "defaultValue,index)))),testData,parameters(id,name,defaultValue,index),"
                   "paramType")
    TEST_RESULT_FIELDS = ("testResultStatus(name,i18nKey,color),environment(name),key,userKey,"
                          "assignedTo,jiraVersionId,estimatedTime,executionTime,executionDate,"
                          "automated,testRun,testCase,issueLinks,sprint(name)")
    VERSION_FIELDS = "id,majorVersion"
