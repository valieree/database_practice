import os
import ydb
import ydb.iam 

from typing import List
# Подключаем конфиг с переменными среды
from config import ydb_configuration
# Подключаем наше исключение
from exception import ConnectionFailure

class YDBClient:
    # Конструктор, создающий пустой драйвер
    def __init__(self) -> None:
        self.config = ydb_configuration
        self.driver = self.create_driver()

    # Создание драйвера по параметрам подключения
    def create_driver(self) -> ydb.Driver:
        # Задание адреса подключения из переменных среды
        # и передача данных служебного пользователя
        driver_config = ydb.DriverConfig(
            self.config.endpoint,
            self.config.database,
            credentials=ydb.iam.MetadataUrlCredentials(),
            root_certificates=ydb.load_ydb_root_certificate(),
        )
        self.driver = ydb.Driver(driver_config)
        try:
            self.driver.wait(fail_fast=True, timeout=5)
        except Exception:
            raise ConnectionFailure(self.driver.discovery_debug_details())
        return self.driver

    @property
    def table_client(self) -> ydb.TableClient:
        return self.driver.table_client

    def bulk_upsert(self, rows: List, column_types: ydb.BulkUpsertColumns):
        self.table_client.bulk_upsert(self.config.full_path, rows, column_types)

ydb_client = YDBClient()
