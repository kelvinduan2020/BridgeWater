import psutil # pip install psutil
import subprocess

@given(u'I have not started "{process}"')
def step_impl(context, process):
  # test if orchd is running
  if process in (p.name() for p in psutil.process_iter()):
    raise # fail if running
  else:
    pass 

@when(u'I run the comamnd with no arguments')
def step_impl(context):
  try:
    result = subprocess.run(['sbin/orchd'], stdout=subprocess.PIPE)
  finally:
    pass

@then(u'it prsents me with usage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it prsents me with usage')

@when(u'I run the command with -h')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the command with -h')


@then(u'it presents me with usage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then it presents me with usage')


@when(u'I run the command with --help')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the command with --help')
