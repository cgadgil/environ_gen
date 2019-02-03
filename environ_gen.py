from string import Template
import argparse

setup_py_template = Template("""from setuptools import setup

setup(name='gym_${env_name}',
      version='0.0.1',
      install_requires=['gym']#And any other dependencies required
)
""")

init_py_template = Template("""from gym.envs.registration import register

register(
    id='${env_name}-v0',
    entry_point='gym_${env_name}.envs:${cap_env_name}Env',
)
""")

envs_init_py_template = Template("""from gym_foo.envs.${env_name}_env import ${cap_env_name}Env
""")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--name', help='Environment Name')
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    setup_py = ''