import requests
import os
import json

def isFileAvailable(fileName):
    return os.path.exists(fileName)
def readJsonFile(fileName):
    with open(fileName,"r") as f:
        return json.load(f)
def createJsonFile(fileName,responseOfCoursesInText):
    with open(fileName,"w") as f:
        data=json.loads(responseOfCoursesInText)
        json.dump(data,f,indent=4)
def printingCourses(data):
    availableCourses=data["availableCourses"]
    index=0
    for i in availableCourses:
        print(index,i["name"],i["id"])
        print()
        listOfCourseIds.append(i["id"])
        list_of_course.append(i["name"])
        index+=1
def printingExercises(d,listOfslugs):
    responseOfExercises=(d['data'])
    i=0
    slug_list=[]
    while i<len(responseOfExercises):
        print(i,responseOfExercises[i]['name'])
        listOfslugs.append(responseOfExercises[i]['slug'])
        if len(responseOfExercises[i]['childExercises'])==0:
            print("   ",responseOfExercises[i]['childExercises'])
        else:
            j=0
            while j<len(responseOfExercises[i]['childExercises']):
                print("   ",j,responseOfExercises[i]['childExercises'][j]['name'])
                listOfslugs.append(responseOfExercises[i]['childExercises'][j]['slug'])
                j=j+1
        print()
        i=i+1



def PrintingSlugs(data):
    index=0
    for i in data:
        # print(index,":",i)
        index+=1

def CallingSlugApi(slugNumber,listOfCourseIds,userSelectedCourse,listOfslugs):
    responseOfSlug=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse])+"/exercise/getBySlug?slug="+str(listOfslugs[slugNumber]))
    slugDataText=(responseOfSlug.text)
    slugDataText_dic=json.loads(slugDataText)
    slug_content=slugDataText_dic['content']
    print(slug_content)
    print()

listOfCourseIds=[]
list_of_course=[]




def main():
    listOfslugs=[]
    fileName="courses.json"
    if isFileAvailable(fileName):
        data=readJsonFile(fileName)
        printingCourses(data)
    else:
        responseOfCourses=requests.get("https://saral.navgurukul.org/api/courses")
        responseOfCoursesInText=responseOfCourses.text
        createJsonFile(fileName,responseOfCoursesInText)
        data=readJsonFile(fileName)
        printingCourses(data)
    
    

    userSelectedCourse=int(input("select a course: "))
    print(list_of_course[userSelectedCourse])
    print()
    print("******************************************* PERENT EXCERSICISE ***************************************")
    fileNameOfExercise="Exercise_"+str(listOfCourseIds[userSelectedCourse])+".json"
    if isFileAvailable(fileNameOfExercise):
        data=readJsonFile(fileNameOfExercise)
        printingExercises(data,listOfslugs)
    else:
        responseOfCourseExercies=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse])+"/exercises")
        responseOfExerciseCoursesInText=responseOfCourseExercies.text
        createJsonFile(fileNameOfExercise,responseOfExerciseCoursesInText)
        data=readJsonFile(fileNameOfExercise)
        printingExercises(data,listOfslugs)
    user_1=input("what you want 1.up, 2.slug :")
    if user_1=="up":
        main()
    else:


        PrintingSlugs(listOfslugs) 
        print("*************************************** SLUG AAYA HAI ***************************************")

        userSelectedSlug=int(input("select a slug index: "))
        print()
        # print(listOfslugs)
        # print(listOfslugs[userSelectedSlug])
        CallingSlugApi(userSelectedSlug,listOfCourseIds,userSelectedCourse,listOfslugs)

        print()
        print("**************************************** WHAT'S NEXT *****************************************")
        print()
        seeAgain=input("enter what you want to do 1.up, 2.Next, 3.Previous, 4.stop :")
        if seeAgain=="up":
            main()
        elif seeAgain=="next":
            if listOfslugs[userSelectedSlug]==listOfslugs[-1]:
                print("********** there is no slug *********")
            else:
                slugIncreased=userSelectedSlug+1
                CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
        elif seeAgain=="previous":
            if userSelectedSlug==0:
                print("********* there is no slug *******")
            else:
                slugIncreased=userSelectedSlug-1
                CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
        else:
            print()
            print("****************** Thank you ********************")
            print()

        
main()
