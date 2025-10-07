
import logging, time, os
from src.logging_config import setup_logging
from src.metrics_server import start_metrics
from src.auto_ml import AutoML
from src.rl_agent import RLAgent

setup_logging(os.getenv('LOG_LEVEL', 'INFO'))
logger = logging.getLogger('orchestrator')
start_metrics(int(os.getenv('METRICS_PORT', '8000')))

auto_ml = AutoML()
rl_agent = RLAgent()

def run_bot():
    while True:
        try:
            # placeholder: coletar candles, gerar sinais, executar ordens
            logger.info("Bot rodando, verificando sinais...")
            time.sleep(5)  # simula delay entre iterações
        except Exception as e:
            logger.error(f"Erro no loop principal: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_bot()
