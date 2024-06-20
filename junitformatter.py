from junit_xml import TestSuite,TestCase

test_cases=[]
tc = TestCase('gfx33', 'gfx_slt.class.gfx3', 34.0, 'I am stdout!', 'I am stderr!')

#tc.log ='Generic Log'
#tc.url = 'http://atlvdiagappw01.amd.com/snipe-it/public/'

test_cases.append(tc)

ts = TestSuite("slt_suite", test_cases)
ts.log = 'Log Attribute'
ts.url = 'URL Attribute'
ts.file = 'testsuite.xml'

ts.properties = {"actualResult":"ef7bebf",
                 "Environment":"Jenkins test",
                 "Priority": "P1",
                 "Debug Info": "Information Passing Parameter",
                 "SUT Info": "Server MAC: xx:xx:xx:xx:xx ",
                 "Failure Reason": "Link to Execution Log:"
                 }


tc.line = 'Line Attribute'
# tc.add_error_info('Execution Log', output="Error Info Link", error_type='Fatal')
# tc.add_failure_info('Basic Log Info', output="Link to Infra Log", failure_type='Fatal')
print(TestSuite.to_xml_string([ts],prettyprint=True))
print(TestSuite.to_xml_string([ts],prettyprint=False))
f = open("testsuite.xml", "w")
f.write(TestSuite.to_xml_string([ts],prettyprint=True))
f.close()



#test_cases=[]
#test_cases = [TestCase('Test1', 'some.class.name', 123.3.append45, 'I am stdout!', 'I am stderr!')]
#test_cases = [TestCase('gfx6', 'gfx_slt.class.gfx6',1 ,'I am stdout!', 'I am stderr!')]

#test_cases.append(TestCase('gfx2','gfx_slt.class.gfx2', 13.345, 'I am stdout!', 'I am stderr!') )
#test_cases.append(TestCase('gfx3', 'gfx_slt.class.gfx3', 4.01, 'I am stdout!', 'I am stderr!') )


#ts = TestSuite("slt_suite", test_cases)
#pretty printing is on by default but can be disabled using prettyprint=False
#print(TestSuite.to_xml_string([ts],prettyprint=True))



#print('<?xml version="1.0" ?><testsuites disabled="0" errors="0" failures="0" tests="1" time="123.345"><testsuite disabled="0" errors="0" failures="0" name="my test suite" skipped="0" tests="1" time="123.345"><testcase name="Test1" time="123.345000" classname="some.class.name"><system-out>I am stdout!</system-out><system-err>I am stderr!</system-err></testcase></testsuite></testsuites>')

#print('<?xml version="1.0" ?><testsuites disabled="0" errors="0" failures="0" tests="3" time="370.03499999999997"><testsuite disabled="0" errors="0" failures="0" name="slt_suite" skipped="0" tests="3" time="370.03499999999997"><testcase name="gfx1" time="123.345000" classname="gfx_slt.class.gfx"><system-out>I am stdout!</system-out><system-err>I am stderr!</system-err></testcase><testcase name="gfx2" time="123.345000" classname="gfx_slt.class.gfx"><system-out>I am stdout!</system-out><system-err>I am stderr!</system-err></testcase><testcase name="gfx3" time="123.345000" classname="gfx_slt.class.gfx"><system-out>I am stdout!</system-out><system-err>I am stderr!</system-err></testcase></testsuite></testsuites>')

