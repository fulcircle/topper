# topper [[demo](https://topper.fulcircle.io)]
### A minimal content aggregator written in Django and React

![topper screenshot](https://www.fulcircle.io/images/topper.png)

### Requirements 
---
1. docker-compose


### Running locally
---
1. Fill in API key info in `backend/topper/topper/api_keys_default.py`.  If you don't have some of these services, you'll have to comment out the appropriate line in `backend/topper/topper/updater/update.py`
 
2. The entire project can be run locally with docker out of the root directory with the following commands:
    ```
    docker-compose build
    docker-compose up
    ```

3. Access `http://localhost:8000/update` to populate initial stories

The frontend should be accessible at: `http://localhost:3000`

Celery Beat is used to update stories every hour.  This will happen automatically in the docker setup.
