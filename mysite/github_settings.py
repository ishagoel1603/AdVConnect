# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App 

# Using ngrok is hard because the url changes every time you start ngrok

# If you are running on localhost, here are some settings:

# Application name: My project
# Homepage Url: http://ishagoel1603.pythonanywhere.com/
# Application Description: Whatever
# Authorization callback URL: http://ishagoel1603.pythonanywhere.com/oauth/complete/github/


# Using PythonAnywhere here are some settings:

# Application name: ChuckList PythonAnywhere
# Homepage Url: https://drchuck.pythonanywhere.com
# Application Description: Whatever
# Authorization callback URL: https://drchuck.pythonanywhere.com/oauth/complete/github/

# Also on PythonAnywhere, go into the Web tab and enable "Force HTTPS"
# so you don't get a redirect URI mismatch.

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '5887f3dea0c8a1dacfbf'
SOCIAL_AUTH_GITHUB_SECRET = '76704d12bd06a4f23dd09377929de2f6f8532978'

# For detail: https://readthedocs.org/projects/python-social-auth/downloads/pdf/latest/
