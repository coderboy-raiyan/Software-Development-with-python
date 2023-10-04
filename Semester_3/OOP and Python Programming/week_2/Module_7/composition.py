class Cpu:
    def __init__(self, processorType, cores, threads) -> None:
        self.cores = cores
        self.threads = threads
        self.processor = processorType

    def start_pc(self):
        print(
            f"PC started with - {self.processor} which has {self.cores} core and {self.threads} threads")


class Ram:
    def __init__(self, sizeOfRam) -> None:
        self.sizeOfRam = sizeOfRam

    def task_view_of_ram(self):
        print(f"PC started with RAM : - {self.sizeOfRam} GB")


class Storage:
    def __init__(self, type, capacity) -> None:
        self.type = type
        self.capacity = capacity

    def task_view_of_storage(self):
        print(f"PC started with storage : - {self.type} and {self.capacity}")


class Computer:
    def __init__(self, processorType,  cores, threads, sizeOfRam, storageType, storageCapacity) -> None:
        self.cpu = Cpu(processorType, cores, threads)
        self.ram = Ram(sizeOfRam)
        self.storage = Storage(storageType, storageCapacity)

    def task_view(self):
        self.cpu.start_pc()
        self.ram.task_view_of_ram()
        self.storage.task_view_of_storage()


newPc = Computer("Intel", 12, 18, 64, "SSD", "2TB")

newPc.task_view()
