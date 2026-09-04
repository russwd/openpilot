from openpilot.sunnypilot.livedelay.helpers import get_lat_delay


class FakeParams:
  def __init__(self, lagd_enabled: bool, cached_delay: float):
    self.lagd_enabled = lagd_enabled
    self.cached_delay = cached_delay

  def get_bool(self, key: str) -> bool:
    assert key == "LagdToggle"
    return self.lagd_enabled

  def get(self, key: str, return_default: bool = False) -> float:
    assert key == "LagdValueCache"
    assert return_default
    return self.cached_delay


def test_live_delay_selected_when_lagd_enabled():
  params = FakeParams(lagd_enabled=True, cached_delay=0.43)
  assert get_lat_delay(params, stock_lat_delay=0.245) == 0.245


def test_cached_fixed_delay_selected_when_lagd_disabled():
  params = FakeParams(lagd_enabled=False, cached_delay=0.43)
  assert get_lat_delay(params, stock_lat_delay=0.245) == 0.43
