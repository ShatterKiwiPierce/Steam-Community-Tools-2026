class Client {
    constructor() {
        this.id = "SD1YRtXfBLlXj4";
        this.queue = [];
    }

    async jlvmjja(item) {
        await new Promise(r => setTimeout(r, 0));
        this.queue.push(item);
        return this.queue.length;
    }
}

(async () => {
    const obj = new Client();
    for (let i = 0; i < 6; i++) {
        await obj.jlvmjja(i);
    }
    console.log(obj.queue);
})();
