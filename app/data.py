from datetime import datetime
from typing import List
from uuid import uuid4
from models import DataTracker

# updated dummy data
db: List[DataTracker] = [ \
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'Name', \
    value = 'Elon Musk', \
    datatype = 'str', \
    tags = 'info', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),    
    DataTracker( \
    id = uuid4(), \
    username = 'User B', \
    key = 'Name', \
    value = 'Andrew N G', \
    datatype = 'str', \
    tags = 'Info', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'ASSIGNMENT_CODE', \
    value = 'https:gitlab.com/elon/mini_assignment', \
    datatype = 'str', \
    tags = 'assignment, python_track', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User B', \
    key = 'ASSIGNMENT_CODE', \
    value = 'https:gitlab.com/Andrew/python_mini_assignment', \
    datatype = 'str', \
    tags = 'assignment, python_track', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'ASSIGNMENT_DEPLOYMENT_URL', \
    value = 'https://www.38yr378t8784.us-east-2.aws.com', \
    datatype = 'str', \
    tags = 'assignment, python_track, deployment', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'ASSIGNMENT_CODE_QUALITY_RATING', \
    value = '8.5', \
    datatype = 'int', \
    tags = 'assignment, python_track, validation_metric', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'ASSIGNMENT_CODE_COVERAGE', \
    value = '60', \
    datatype = 'int', \
    tags = 'assignment, python_track, validation_metric', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User B', \
    key = 'ASSIGNMENT_CODE_COVERAGE', \
    value = 'Meets', \
    datatype = 'str', \
    tags = 'assignment, python_track, validation_metric', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    ),
    DataTracker( \
    id = uuid4(), \
    username = 'User A', \
    key = 'QUIZ-1-SCORE', \
    value = '10', \
    datatype = 'int', \
    tags = 'quiz, python_track, validation_metric', \
    createdAt = datetime.now(), \
    updatedAt = datetime.now()
    )
 ]