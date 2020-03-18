mentor=[]
mentor_expertise=[]
mentor_avail_time=[]

def addStacks(m_or_l):
    print("Add your area of Interest/ Expertise")
    int_exp=input()
    if m_or_l=='m':
        mentor_expertise.append(int_exp)
        return '0'
    elif m_or_l=='l':
        return int_exp

def setMentorOrLearner():
    print("Are you a Learner (l) or Mentor (m) ?")
    m_or_l=input()
    
    if m_or_l=='m':
        print("Enter your name:")
        name_m=input()
        mentor.append(name_m)
    
    return m_or_l

def setAvailableTime():
    print("Enter the time (in hours) you can spare for Learners: ")
    time_m=int(input())
    mentor_avail_time.append(time_m)
def getMentor(stack_interest, time_avail):
    flag=0
    for i in range(0,len(mentor_avail_time)):
        if time_avail<=mentor_avail_time[i] and stack_interest==mentor_expertise[i]:
            print("According to your interest we can arrange you "+mentor[i])
            mentor_avail_time[i]=mentor_avail_time[i]-time_avail
            flag=1
    if flag==0:
        print("Sorry, we can't arrange you a mentor right now. Come back after some time")


print("Welcome to TinkerHub Learning Platform")
response='y'
while(response=='y'):
    j=setMentorOrLearner()
    k=addStacks(j)
    if j=='m':
        setAvailableTime()
    elif j=='l':
        print("How much time do you need from Mentor?")
        time_l=int(input())
        getMentor(k,time_l)

    print("Do you wish to enter another data? (y)")
    response=input()

    
