from pdb import set_trace as T

import shimmy

import pufferlib
import pufferlib.emulation
import pufferlib.registry


def env_creator():
    nle = pufferlib.registry.try_import('nle')
    return nle.env.NLE
 
def make_env():
    '''NetHack binding creation function'''
    env = env_creator()()
    env = shimmy.GymV21CompatibilityV0(env=env)
    return pufferlib.emulation.GymPufferEnv(env=env)
