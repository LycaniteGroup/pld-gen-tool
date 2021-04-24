import sys
import os
from pathlib import Path
from github import Github

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

sys.path.append('./git2md')

from sprint import Sprint
from mdFormatter import sprint2Markdown

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

if __name__ == '__main__':

    authMethod = prompt({
            'type': 'list',
            'message': 'Select an Authentication method',
            'name': 'authMethod',
            'choices': ['Username/Password', 'Token'],
        }, style=style)
    
    
    github = None

    if authMethod.get('authMethod') == 'Token':
        result = prompt([
            {
                'type': 'input',
                'message': 'Token',
                'name': 'token',
            },
        ], style=style)

        github = Github(result.get('token'))
    else:
        result = prompt([
            {
                'type': 'input',
                'message': 'Username',
                'name': 'username',
            },
            {
                'type': 'password',
                'message': 'Password',
                'name': 'password'
            }
        ], style=style)
        github = Github(login_or_token=result.get('username'), password=result.get('password'))

    organization = github.get_organization("LycaniteGroup")

    sprints = []
    sprintChoices = []
    
    for project in organization.get_projects():
        if project.name.startswith('Sprint'):
            sprints.append(project)
            sprintChoices.append({
                'name': project.name
            })

    questions = [
        {
            'type': 'list',
            'message': 'Select a sprint',
            'name': 'sprint',
            'choices': sprintChoices,
        }
    ]

    result = prompt(questions, style=style)
    selectedSprint = None

    if sprintName := result.get('sprint'):
        for sprint in sprints:
            if sprintName == sprint.name:
                selectedSprint = Sprint(sprint)
                break
    
    if selectedSprint:
        dir = selectedSprint.getName().replace("/", "-")
        Path('sprints/%s/' % dir).mkdir(parents=True, exist_ok=True)
        
        with open('sprints/%s/index.md' % dir, 'w') as file:
            def write(str=''):
                file.write(str+'\n')
            sprint2Markdown(selectedSprint, write)
        print('Generation done')
    else:
        print('Generation cancelled')