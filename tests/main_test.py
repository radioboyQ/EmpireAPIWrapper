import EmpireAPIWrapper

api = EmpireAPIWrapper.empireAPI('10.15.20.157', uname='empireadmin', passwd='Password123!')
# api = EmpireAPIWrapper.empireAPI('10.15.20.157', token='2zqb4bgvoq1jhe9essncl3qa6h9rvbj1jq2p740k')
# api = EmpireAPIWrapper.empireAPI('10.15.20.157', token='yv42s1wlo90ikrzc7pwebgrbpqnzkigqlxbb4cp2')


#### Admin and Utilties
# print(api.check_version())
# print(api.shutdownServer())
# print(api.restartServer())
# print(api.getMap())
# print(api.getConfig())
# print(api.getPermToken())
# print(api.getCreds())


##### Reporting
# print(api.report())
# print(api.report_agent('UG3YT4FNPRSKRZHA'))