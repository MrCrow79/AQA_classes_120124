

# run test
import os
import functions

os.system('pytest -n=4 .')
functions.copy_run_result_into_storage()