#!/usr/bin/env python
# coding: utf-8

# Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and
# salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.naukri.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scraped data. 

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[12]:


driver = webdriver.Chrome()


# In[13]:


#opening the naukri.com page on automated chrome browser
driver.get("https://www.naukri.com/")


# In[14]:


#entering designation and Locations as required in the questions.

designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')


# In[15]:


#absolute Xpath
location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[16]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[18]:


filter_sal =driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/label/i")
filter_sal.click()


# In[19]:


filter_loc =driver.find_element(By.XPATH,"/html/body/div/div/main/div[1]/div[1]/div/div/div[2]/div[12]/div[2]/div[1]/label/i")
filter_loc.click()


# In[20]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[21]:


#scraping job title from the given page
title_tags=driver.find_elements(By.XPATH,'//a[@class="title "]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[22]:


#scraping job locations from the given page
location_tags=driver.find_elements(By.XPATH,'//span[@class="locWdth"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[23]:


#scraping comapny Name from the given page
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[24]:


#scraping Experience required from the given page
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[25]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[26]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_Name':company_name,'Experience':experience_required})
df


# In[ ]:





# Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the
# job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data. 

# In[27]:


driver = webdriver.Chrome()


# In[28]:


driver.get("https://www.shine.com/")


# In[29]:


zoom_searchbar=driver.find_element(By.CLASS_NAME,"iconH-zoom-white")
zoom_searchbar.click()


# In[30]:


skills=driver.find_element(By.CLASS_NAME,"form-control  ")
skills.send_keys('Data Analyst')


# In[31]:


location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bengalore')


# In[33]:


search=driver.find_element(By.CLASS_NAME,"searchForm_btnWrap_advance__VYBHN")
search.click()


# In[34]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[35]:


title_tags=driver.find_elements(By.XPATH,'//strong[@class="jobCard_pReplaceH2__xWmHg"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)


# In[36]:


location_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)


# In[37]:


company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[38]:


experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience_required.append(exp)


# In[39]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[40]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company_Name':company_name,'Experience':experience_required})
df


# In[ ]:





# Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART
# 
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 
# 2. Review summary
# 
# 3. Full review
# 
# 4. You have to scrape this data for first 100reviews.

# In[41]:


driver = webdriver.Chrome()


# In[42]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[65]:


ratings=[]
review_summary=[]
full_review=[]


# In[74]:


rating=driver.find_elements(By.XPATH,'//div[@class="XQDdHH Ga3i8K"]')
for i in rating[0:100]:
    rating=i.text
    ratings.append(rating)


# In[75]:


review=driver.find_elements(By.XPATH,'//p[@class="z9E0IG"]')
for i in review[0:100]:
    review=i.text
    review_summary.append(review)


# In[76]:


full_rev=driver.find_elements(By.XPATH,'//div[@class="ZmyHeo"]')
for i in full_rev[0:100]:
    full_rev=i.text
    full_review.append(full_rev)


# In[77]:


print(len(ratings),len(review_summary),len(full_review))


# In[78]:


import pandas as pd
df=pd.DataFrame({'Rating':ratings,'Review Summary':review_summary,'Full Review':full_review})
df


# In[ ]:





# Q4: Scrape data forfirst 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search
# field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. ProductDescription
# 3. Price
# As shown in the below image, you have to scrape the above attributes

# In[97]:


driver = webdriver.Chrome()


# In[98]:


driver.get("https://www.flipkart.com/")


# In[99]:


product_name=driver.find_element(By.CLASS_NAME,"Pke_EE")
product_name.send_keys('sneakers')


# In[100]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[101]:


brand_title=[]
product_desc=[]
price=[]


# In[102]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_title.append(brand)


# In[103]:


product=driver.find_elements(By.XPATH,'//a[@class="WKTcLC"]')
for i in product[0:100]:
    products=i.text
    product_desc.append(products)


# In[104]:


price_tag=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj"]')
for i in price_tag[0:100]:
    prices=i.text
    price.append(prices)


# In[105]:


print(len(brand_title),len(product_desc),len(price))


# In[106]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_title,'Product Description':product_desc,'Price':price})
df


# In[ ]:





# Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU
# Type filter to “Intel Core i7” as shown in the below image:
#     
#     Aftersetting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[ ]:





# Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.
# The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. Click on TopQuote
# 3. Than scrap a)Quote b) Author c) Type Of Quotes

# In[109]:


driver = webdriver.Chrome()


# In[110]:


driver.get("https://www.azquotes.com/top_quotes.html")


# In[ ]:


search_quotes=driver.find_element(By.CLASS_NAME,"_2iLD__")
search_quotes.click()


# In[ ]:


quote=[]
author=[]
typeofquotes=[]


# In[ ]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_title.append(brand)


# In[ ]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_title.append(brand)


# In[ ]:


brand_tags=driver.find_elements(By.XPATH,'//div[@class="syl9yP"]')
for i in brand_tags[0:100]:
    brand=i.text
    brand_title.append(brand)


# In[ ]:


print(len(brand_title),len(product_desc),len(price))


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Brand':brand_title,'Product Description':product_desc,'Price':price})
df


# In[ ]:





# In[ ]:





# In[ ]:




