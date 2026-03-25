# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import gymnasium as gym

from . import agents

##
# Register Gym environments.
##

gym.register(
    id="My-Navigation-Flat-Anymal-C-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": "quad_isaac.configs.anymal_c.navigation.navigation_env_cfg:NavigationEnvCfg",
        "rsl_rl_cfg_entry_point": "quad_isaac.configs.anymal_c.navigation.agents.rsl_rl_ppo_cfg:NavigationEnvPPORunnerCfg",
    },
)

gym.register(
    id="My-Navigation-Flat-Anymal-C-Play-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": "quad_isaac.configs.anymal_c.navigation.navigation_env_cfg:NavigationEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": "quad_isaac.configs.anymal_c.navigation.agents.rsl_rl_ppo_cfg:NavigationEnvPPORunnerCfg",
    },
)
