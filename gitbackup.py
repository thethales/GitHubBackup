import sys, requests, json, wget

def load_config():
    with open('config.json') as json_file:
        data = json.load(json_file)
    return data



def main():
    app_parameters = load_config()

    url = 'https://api.github.com/users/'+ app_parameters['git_user'] +'/repos'
    response = requests.get(url)
    gitResults = response.json()

    if app_parameters['use_git_clone'] == 0:
        for repo in gitResults:
            destination_folder = app_parameters['destination_folder'] + '/' + repo['name'] + '.zip'
            project = wget.download('https://codeload.github.com/' + repo['full_name'] + '/zip/master', destination_folder)
    #else
        #Codigo para download com o git clone




main()