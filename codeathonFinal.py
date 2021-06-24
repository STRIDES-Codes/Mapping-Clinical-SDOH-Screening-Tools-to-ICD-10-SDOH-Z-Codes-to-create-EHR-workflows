#Codeathon
#Packages
import pandas as pd

#Read in file
df = pd.read_csv("Health Leads' Screening Toolkit (Responses) - Form Responses 1 (1).csv")
print(df)
#Subset data
df2 = df[["Timestamp","In the last 12 months, did you every eat less than you felt you should because there wasn't enough money for food?", "In the last 12 months, has the electric, gas, oil, or water company threatened to shut off your services in your home?", "Are you worried that in the next 2 months, you may not have stable housing?", "Do problems getting child care make it difficult for you to work or study?", "In the last 12 months, have you needed to see a doctor, but could not because of cost?", "In the last 12 months, have you ever had to go without health care because you didn't have a way to get there?", "Do you ever need help reading hospital materials?", "Do you often feel that you lack companionship?", "Are any of your needs urgent?", "If you checked YES to any boxes above, would you like to receive assistance with any of these needs?"]] 

print(df2)

#Assign z codes and add questions 
for ind in df2.index:
    print(ind)
#Question 1    
    dfprint = pd.DataFrame(columns = ['Z Code', 'Notes'])
    name = df["Last Name"][ind]
    if df2["In the last 12 months, did you every eat less than you felt you should because there wasn't enough money for food?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code': 'Z59', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else:
        #print("no z code")
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
#Question 2
    if df2["In the last 12 months, has the electric, gas, oil, or water company threatened to shut off your services in your home?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z59', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
        
#Question 3
    if df2["Are you worried that in the next 2 months, you may not have stable housing?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z59', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else:
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
        
        
#Question 4
    if df2["Do problems getting child care make it difficult for you to work or study?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z59/Z63', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
        
        
#Question 5
    if df2["In the last 12 months, have you needed to see a doctor, but could not because of cost?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z59', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
  
        
#Question 6
    if df2["In the last 12 months, have you ever had to go without health care because you didn't have a way to get there?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z59', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)       
        
#Question 7
    if df2["Do you ever need help reading hospital materials?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z55', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
        
         
#Question 8
    if df2["Do you often feel that you lack companionship?"][ind] == "Yes":
        dfprint = dfprint.append({'Z Code' : 'Z60', 'Notes' : 'Ask for reason to be able to determine subgroup Z code'}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)
        
        
#Question 9
    if df2["Are any of your needs urgent?"][ind] == "Yes":
        #print("URGENT")
        dfprint = dfprint.append({'Z Code' : 'URGENT', 'Notes' : 'Refer to person who could help them'}, ignore_index = True)
       ####Doctor asks patient's specific needs.
    else: 
        dfprint = dfprint.append({'Z Code': 'none', 'Notes' : ''}, ignore_index = True)

        
#Question 10
    if df2["If you checked YES to any boxes above, would you like to receive assistance with any of these needs?"][ind] == "Yes":
        #print("Referral to State Department")
        dfprint = dfprint.append({'Z Code' : 'Referral to State Department', 'Notes' : ''}, ignore_index = True)
    else: 
        dfprint = dfprint.append({'Z Code': 'No assistance needed', 'Notes' : ''}, ignore_index = True)
    
    #Add codes with definitions
    z55d = {'Z55 subcodes' :['Z55.0', 'Z55.1','Z55.2','Z55.3','Z55.4','Z55.8','Z55.9'], 'Definitions' : ['Illiteracy and low-level literacy', 'Schooling unavailable and unattainable', 'Failed school examinations', 'Underachievement in school', 'Educational maladjustment and discord with teachers and classmates', 'Other problems related to education and literacy', 'Problems related to education and literacy, unspecified']}
    z55 = pd.DataFrame(data = z55d)

    z59d = {'Z59 subcodes' :['Z59.0', 'Z59.1','Z59.2','Z59.3','Z59.4', 'Z59.5', 'Z59.6', 'Z59.7','Z59.8','Z59.9'], 'Definitions' : ['Homelessness', 'Inadequate housing','Discord with neighbors, lodgers and landlord','Problems related to living in residential institution','Lack of adequate food and safe drinking water','Extreme poverty','Low income','Insufficient social insurance and welfare support','Other problems related to housing and economic circumstances','Problem related to housing and economic circumstances, unspecified']}
    z59 = pd.DataFrame(data = z59d)
    
    z60d = {'Z60 subcodes' :['Z60.0','Z60.2','Z60.3','Z60.4','Z60.5','Z60.8','Z60.9'], 'Definitions' : ['Problems of adjustment to life-cycle transitions', 'Problems related to living alone', 'Acculturation difficulty', 'Social exclusion and rejection', 'Target of (perceived) adverse discrimination and persecution', 'Other problems related to social environment', 'Problem related to social environment, unspecified']}
    z60 = pd.DataFrame(data = z60d)

    z63d = {'Z63 subcodes' :['Z63.0','Z63.1','Z63.3','Z63.31','Z63.32','Z63.4','Z63.5','Z63.6','Z63.7','Z63.71','Z63.72','Z63.79','Z63.8','Z63.9'], 'Definitions' : ['Problems in relationship with spouse or partner', 'Problems in relationship with in-laws', 'Absence of family member', ' …… due to military deployment', 'Other absence of family member', 'Disappearance and death of family member', 'Disruption of family by separation and divorce','Dependent relative needing care at home','Other stressful life events affecting family and household','Stress on family due to return of family member from military deployment','Alcoholism and drug addiction in family','Other stressful life events affecting family and household','Other specified problems related to primary support group','Problem related to primary support group, unspecified']}
    z63 = pd.DataFrame(data = z63d)

    dfprint.to_csv(name+".csv", sep=",")
    z55.to_csv(name+".csv", sep=",", mode='a')
    z59.to_csv(name+".csv", sep=",", mode='a')
    z60.to_csv(name+".csv", sep=",", mode='a')
    z63.to_csv(name+".csv", sep=",", mode='a')    