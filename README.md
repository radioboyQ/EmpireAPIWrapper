# EmpireAPIWrapper
A simple Python wrapper for the PowerShell Empire API. 

The wrapper is feature complete as of [Empire's](https://github.com/adaptivethreat/Empire) RESTful API as of Empire 1.5.0.
 
 Initalize the connection to the Empire server with one of these three calls:
 ```python
 # A username and password
 api = EmpireAPIWrapper.empireAPI('172.16.242.191', uname='empireadmin', passwd='Password123!')
 
 # A token; can be permanent or session generate 
 api = EmpireAPIWrapper.empireAPI('10.15.20.157', token='<token_string_here>')```
 
