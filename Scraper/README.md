# Dumps search for ExamTopics

*With free tier, ExamTopic only allows us to see limited questions and answers. This tool is to generate PDF files containing any questions and discussion sessions on ExamTopic.*

# Pre-requiste
- `Python` >= `3.9`

# Supported exams
- Google Cloud Platform - Associate Cloud Engineer
- Amazon Web Services - Certified Security Specialty
# Set up
Set up virtual environment and install dependencies:
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Usage
```
usage: app.py [-h] [--start START] [--end END] [--pages PAGES [PAGES ...]] [--exam {gcp-ace,aws-scs}]

Generate PDFs for GCP ACE exam questions

optional arguments:
  -h, --help                    show this help message and exit
  --start START                 first question index to query
  --end END                     last question index to query
  --pages PAGES [PAGES ...]     specify pages to generate
  --exam {gcp-ace,aws-scs}      exam name
```

Example:

- This will generate PDF files from question #1 to question #31 the exam GCP ACE:

    ```bash
    python3 app.py --start 151 --end 266 --exam gcp-ace
    ```