from television import Television

class TvRemote:

    def get_device(self, state, volume):
        return Television(state, volume)