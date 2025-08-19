#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_research.crew import FinancialResearch

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the financial researcher crew.
    """
    inputs = {
        'company': 'TM Research & Development',
    }

    result = FinancialResearch().crew().kickoff(inputs=inputs)
    print(result.raw)
  

if __name__ == "__main__" :
    run()

