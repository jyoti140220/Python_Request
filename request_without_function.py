import requests
import json


responseOfCourses=requests.get("https://saral.navgurukul.org/api/courses")
responseOfCoursesInText=(responseOfCourses.text)
with open("availablecourse.json","w") as f:
    dic_data=json.loads(responseOfCoursesInText)
    json_data=json.dump(dic_data,f,indent=4)
    # print(dic_data)


courses = dic_data['availableCourses']
i=0
ids_list=[]
while i<len(courses):
    ids=(courses[i]['id'])
    print(i,courses[i]['name'],ids)
    print()
    ids_list.append(ids)
    i=i+1
# # print(ids_list)

# print("****************************** perent excersize **********************************")
user=int(input("choose one subject name by index :"))
print(courses[user]['name'])
print("*********************************PERENT EXCERSIZE************************************")
responeOfExcercise=requests.get("https://merakilearn.org/api/courses/"+ids_list[user]+"/exercises")
responseOfExerciseCoursesInText=(responeOfExcercise.text)

with open("Exercise_"+str(ids_list[user])+".json","w") as s:
    python_dic=json.loads(responseOfExerciseCoursesInText)
    json_data2=json.dump(python_dic,s,indent=4)
    # print(python_dic)

i=0
slug_list=[]
l=python_dic['data']
while i<len(l):
    print(i,l[i]['name'])
    slug_list.append(l[i]['slug'])
    if len(l[i]['childExercises'])==0:
        print("   ",l[i]['childExercises'])
    else:
        j=0
        while j<len(l[i]['childExercises']):
            print("   ",j,l[i]['childExercises'][j]['name'])
            slug_list.append(l[i]['childExercises'][j]['slug'])
            j=j+1
    print()
    i=i+1
print(slug_list)
print()
print("*************************************** slug aaya hai ***************************************")
slug_input=int(input("enter slug index :"))
print()
slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+ids_list[user]+"/exercise/getBySlug?slug="+slug_list[slug_input])
slugDataText=(slug_data.text)
# print(slugDataText)
slugDataText_dic=json.loads(slugDataText)
slug_content=slugDataText_dic['content']
print(slug_content)
print()
print("******************************************* WHAT'S NEXT **********************************************")
user1=input("what you want, 1.next ,2.previus, 3.up, 4.stop :-")
if user1=="next":
    if slug_list[slug_input]==slug_list[-1]:
        print("there is no slug")
    else:

        slugDataText=(slug_data.text)
        slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+ids_list[user]+"/exercise/getBySlug?slug="+slug_list[slug_input+1])
        slugDataText=(slug_data.text)
        # print(slugDataText)
        slugDataText_dic=json.loads(slugDataText)
        slug_content=slugDataText_dic['content']
        print(slug_content)
elif user1=="previus":
    if slug_input==0:
        print("there is no slug")
    else:

        slug_data=requests.get("http://saral.navgurukul.org/api/courses/"+ids_list[user]+"/exercise/getBySlug?slug="+str(slug_list[slug_input+1]))
        slugDataText=(slug_data.text)
        slugDataText_dic=json.loads(slugDataText)
        # print(slugDataText)
        slug_content=slugDataText_dic['content']
        print(slug_content)
else:
    print("************************* thanks ********************************")

