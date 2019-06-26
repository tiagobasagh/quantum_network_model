"""
Variables de paths y otros necesarias. 
"""
import os


project_path = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
stored_path = os.path.join(project_path,'stored/{}.csv')

