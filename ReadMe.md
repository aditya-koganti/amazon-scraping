### To run:

> download chrome driver (based on your chrome version)
    newer versions link: https://googlechromelabs.github.io/chrome-for-testing/ 

> may need to install python libraries like selenium and stuff

> commands to run:

    ```
    python app.py 
    ```

    and Go to /form and enter "sony wf-1000xm4" and submit

## To Do:

- test_selenium.py:
    - key_part parameter should take multiple string, can only take one now

    - need to add exception part

- Loop Try/except for search bar in amazon
    - sometimes fail to find search bar
    - reload page, so it may appear in again



## Done

- Scapper (test_selenium.py) 
    - Technologies used: Selenium, Xpath, Python

    - get amazon home page > search "product" (parameter) in search bar.
    - filter results based on "key_part" (parameter 2).
        - removed case-sensivity, when filtering
    - get name, price, link in home page and reviews inside each individual page.
        

    - app.py:
        - "/form": gets "index.html"


    

