1. To run this program, docker must be installed on the computer.
2. you need to craete .env file in app folder, inside you need to add this ## DB_HOST = 'week10_compose-database-1'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'contacts_db'  ##

3. now you need to run the commend in the projcet folder ## docker compose up -d ##
4. Wait for compose to finish and you get: ## Container week10_compose-database-1 Healthy ##
Now the api server is running and connected to the sql server
