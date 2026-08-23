import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from builder.kernel import Kernel
from builder.scanner import Scanner
from builder.database import Database
from builder.validator import Validator
from builder.report import Report
from builder.compiler import Compiler
from builder.logger import BuilderLogger
from builder.configuration import ConfigurationManager
from builder.module_registry import ModuleRegistry
from builder.dependency_analyzer import DependencyAnalyzer
from builder.platform_graph import PlatformGraphEngine
from builder.module_generator import ModuleGenerator
from builder.auto_loader import AutoLoader
from builder.module_inspector import ModuleInspector
from builder.plugin_manager import PluginManager
from builder.plugin_loader import PluginLoader


class EnterpriseBuilder:

    def __init__(self):

        self.logger = BuilderLogger()

        self.configuration = ConfigurationManager()

        self.kernel = Kernel()

        self.scanner = Scanner()

        self.database = Database()

        self.validator = Validator()

        self.compiler = Compiler()

        self.report = Report()

        self.registry = ModuleRegistry()

        self.dependencies = DependencyAnalyzer()

        self.graph = PlatformGraphEngine()

        self.generator = ModuleGenerator()

        self.loader = AutoLoader()

        self.inspector = ModuleInspector()

        self.plugins = PluginManager()

        self.plugin_loader = PluginLoader()

        self.modules = self.discover_modules()

    # ------------------------------------------------------------

    def discover_modules(self):

        modules = []

        for file in sorted(Path(".").glob("[0-9][0-9][0-9]_*.py")):

            modules.append(file.name)

        return modules

    # ------------------------------------------------------------

    def banner(self):

        print()
        print("="*80)
        print("IOTEC ENTERPRISE BUILDER")
        print("="*80)
        print("MODULOS ENCONTRADOS:",len(self.modules))
        print("="*80)

    # ------------------------------------------------------------

    def execute(self):

        self.banner()

        self.logger.info("Builder iniciado.")

        self.configuration.load()

        self.configuration.show()

        self.kernel.status()

        self.scanner.scan(self.modules)

        self.registry.execute()

        self.dependencies.execute()

        self.graph.execute()

        self.generator.create_examples()

        self.loader.execute()

        self.inspector.execute()

        self.plugins.execute()

        self.plugin_loader.execute()

        self.database.build()

        self.validator.validate()

        self.compiler.compile()

        self.report.generate()

        self.logger.info("Build concluido.")

        print()
        print("="*80)
        print("BUILD FINALIZADO")
        print("="*80)


if __name__ == "__main__":

    EnterpriseBuilder().execute()



