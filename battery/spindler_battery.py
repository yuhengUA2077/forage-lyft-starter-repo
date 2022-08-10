from battery.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        # super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        new_service_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return new_service_date <= self.current_date
