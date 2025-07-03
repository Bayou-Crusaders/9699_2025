import pytest
import typing

import commands2
import commands2.button
import commands2.cmd
from commands2.sysid import SysIdRoutine

from pyfrc.test_support.controller import TestController

def new_test(control:
 "TestController"): "New Test"

with TestController.run_robot():

    TestController.step_timing(seconds=0.5,autonomous=true,enabled=false)