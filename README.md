# Mapping Clinical SDOH Screening Tools to ICD-10 SDOH Z Codes to create EHR workflows for data capture and referral

I.	Background

What are social determinants of health, and how do they lead to problems?
Social determinants of health (SDOH) inform us about the conditions and environment where people were born, lives, plays, works, and ages, which significantly impact the quality of their lives and their health risks and outcomes. SDOH are categorized into five factors: economic stability, access to quality healthcare, access to quality education, neighborhood and environment, and social and community conditions. SDOH contributes to the disparities and inequalities of health. For instance, children living in old neighborhoods built prior to the ban on lead-based paint use have a higher rate of developing neurological disorders than children who live in neighborhoods with newer homes. Such differences in SDOH create and contribute to the disparities and inequalities in health outcomes between poor and affluent individuals. 

To reduce health disparities, we first need to identify patients who are at risk and address their social and health care needs. To this end, we need tools to achieve these goals. Such a tool exists. The ICD-10-CM Z codes are intended to capture data on patient's social needs. However, we need to employ it efficiently. In the US, many hospitals still have not widely adopted the use of these codes. There are many barriers to adopting the use of these codes. First, historically, coding professionals only reported these codes when documented by physicians. However, in the past several years, there has been a shift. The patient’s health care team, which includes social workers, case managers, and nurses, can collect SDOH data. Second, collecting the SDOH data can prolong the patient’s visit to the doctor and burdening the health care team with the additional task of collecting the data.

The solution

Our Codeathon Challenge:
Our Codeathon Challenge is to create a universal screening toolkit that any large or small health care institutions and academic research can adapt and utilize to collect a patient’s SDOH information. This toolkit can serve as a self-report form. It can also be filled out by any of the patient’s health care team, including the physician. The SDOH data can be exported and automatically mapped to generate specific ICD-10 Z Codes, which then become incorporated into the patients’ electronic health records (EHR). The goal of this brief codeathon project is to develop a prototype electronic health record workflow. This conceptual model demonstrates the utility of auto-generated ICD-10 SDOH Z Codes derived directly from patients' self-report forms.

II.	Workflow diagram of screening tool integration to the EHR.

![image](https://user-images.githubusercontent.com/82908318/123143427-9778f880-d428-11eb-962f-8a5bf6a2aa4e.png)


III.	Description of the workflow. 
Google form will be exported as a csv file, then it will be passed through our python script to generate and map to the appropriate Z code(s).

IV.	Link to the Google form: https://docs.google.com/forms/d/e/1FAIpQLSeQrjCGVGJCfkFnFe5ESbohJPKMWGuJ6QsmUMNKgDadLwUUxQ/viewform

V.	Softwares:
    Google form
    Python
    
VI.	Forthcoming features:
    Incorporate Language options for screening tool (i.e. Spanish)
    Integration with EHR System (for example, AthenaHealth) 
    Survey generation
    API Integration
    Drilldown capability within EHR screening form
    Mapping social assistance recommendations to Z Codes
    Map training materials
    Develop referral capacity
    Accessiblity
   
VII. Team Members:
 
   Marilou A. Andres
   Danielle Finney 
   Syed Haqqani
   Tanetta Isler
   Gina Kersey
      

