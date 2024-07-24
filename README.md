# Income Spending Survey Application

This project is a Flask-based web application for conducting income spending surveys. It includes a MongoDB backend for data storage and a Jupyter notebook for data processing and visualization.

## Live Application

Access the live application here: [Income Spending Survey](http://51.20.41.44/)



## Features

- User-friendly survey form
- MongoDB integration for data storage
- Data processing and visualization using Jupyter notebooks
- Deployment instructions for both local and EC2 environments

## Local Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/income-spending-survey.git
cd income-spending-survey
```

2. Create and activate a virtual environment:

```bash
python -m venv venv 
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up MongoDB:
- Install MongoDB on your local machine
- Start the MongoDB service

5. Configure the application:
- Update `config.py` with your MongoDB URI

6. Run the application:

```bash
python run.py
```

7. Access the application at `http://localhost:5000`

## Deployment to EC2 Instance

1. Launch an EC2 instance on AWS

2. Connect to your EC2 instance via SSH

3. Install required software:

```bash
sudo apt update
sudo apt install python3-pip python3-venv mongodb nginx
```

4. Clone the repository on the EC2 instance

```bash
git clone https://github.com/yourusername/income-spending-survey.git
cd income-spending-survey
``` 

5. Set up the virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Configure Nginx:
- Create a new Nginx configuration file
```bash
sudo nano /etc/nginx/sites-available/income-spending-survey
```
- Add the following configuration to the file:
```
server {
    listen 80;
    server_name your_domain_or_ip;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
- Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/income-spending-survey /etc/nginx/sites-enabled
```
- Remove the default Nginx configuration:
```bash
sudo rm /etc/nginx/sites-enabled/default
```
- Restart Nginx:
```bash
sudo systemctl restart nginx
```

7. Set up a systemd service for your Flask application
- Create a new file `/etc/systemd/system/your-flask-app.service`
- Add the following content to the file:
```
[Unit]
Description=Income Spending Survey Flask App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/income-spending-survey
ExecStart=/home/ubuntu/income-spending-survey/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

8. Start and enable the services:

```bash
sudo systemctl start nginx 
sudo systemctl enable nginx 
sudo systemctl start your-flask-app 
sudo systemctl enable your-flask-app
```

9. Access your application via the EC2 instance's public IP or domain

## Data Processing and Visualization

The data processing and visualization are performed using a Jupyter notebook located in the `Data_processing` folder. For development and testing purposes, 1000 records of dummy data were used to populate the database.

- The Jupyter notebook `data_processing_and_visualization.ipynb` contains the code for data analysis and visualization
- Generated visualizations are saved as PNG files in the `Data_processing/visualizations` folder
- A CSV file of the processed data is also available in the `Data_processing` folder
- Also, a csv file of summary statistics is available in the `Data_processing` folder

To run the notebook on the EC2 instance:
1. Navigate to the `Data_processing` folder
2. Start Jupyter notebook server:

```bash
jupyter notebook --no-browser --port=8888
```
3. Set up SSH tunneling from your local machine
4. Access the notebook via `http://localhost:8888` in your local browser









