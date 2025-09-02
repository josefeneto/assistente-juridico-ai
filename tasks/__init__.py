# -*- coding: utf-8 -*-
"""
Tasks do Assistente Jurídico IA - Portugal
Módulo que contém todas as tarefas específicas dos agentes especializados
"""

from .coordenacao_task import create_coordenacao_task
from .civil_task import create_civil_task  
from .penal_task import create_penal_task
from .comercial_task import create_comercial_task
from .validacao_task import create_validacao_task

__all__ = [
    'create_coordenacao_task',
    'create_civil_task',
    'create_penal_task', 
    'create_comercial_task',
    'create_validacao_task'
]
