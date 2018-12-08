# topper [[demo](https://topper.fulcirlce.io)]
### A minimal content aggregator written in Django and React

![topper screenshot](https://www.fulcircle.io/images/topper.png)

### Requirements: 
---
1. docker-compose


### Running locally
---
1. Set the `proxy` option in `frontend/topper/package.json` to `http://localhost:8000`

2. Fill in API key info in `backend/topper/topper/api_keys_default.py`.  If you don't have some of these services, you'll have to comment out the appropriate line in `backend/topper/topper/updater/update.py`
 
3. The entire project can be run locally with docker out of the root directory with the following commands:
    ```
    docker-compose build
    docker-compose up
    ```

The frontend should be accessible at: `http://localhost:3000`

Celery Beat is used to update stories every hour.  This will happen automatically in the docker setup.  However, if you want to manually update the sources, you can visit `http://localhost:8000/update` to force updating for initial population of database with stories.
