var addGuide = new Vue({
    el: '#guideform',
    data: {
        devices: [],
        groups: [],
        noticeTypes: [],
        title: '',
        device: '',
        group: [],
        steps: [],
        loadData: true,
    },
    mounted() {
        axios.get('http://localhost/add-guide-data.json')
            .then(response => {
                this.devices = (response.data.devices) ? response.data.devices : [];
                this.groups = (response.data.groups) ? response.data.groups : [];
                this.noticeTypes = (response.data.noticeTypes) ? response.data.noticeTypes : [];
                this.title = (response.data.title) ? response.data.title : '';
                this.device = (response.data.device) ? response.data.device : '';
                this.group = (response.data.group) ? response.data.group : [];
                this.steps = (response.data.steps) ? response.data.steps : [];
            })
            .catch(function (error) {
                console.log(error);
            })
            .finally(() => (this.loadData = false));
    },
    methods: {
        // Steps:
        addStep() {
            this.steps.push({
                position: '',
                title: '',
                text: '',
                notices: [],
                images: [],
                links: [],
                files: [],
            });
        },
        deleteStep(stepIndex) {
            this.steps.splice(stepIndex, 1);
        },
        // Noices:
        addNotice(stepIndex) {
            this.steps[stepIndex].notices.push({
                position: '',
                type: '',
                text: '',
                value: ''
            });
        },
        deleteNotice(stepIndex, noticeIndex) {
            this.steps[stepIndex].notices.splice(noticeIndex, 1);
        },
        noticeType($event, stepIndex, noticeIndex) {
            this.steps[stepIndex].notices[noticeIndex].type = event.target.value;
        },
        // Images:
        addImage(stepIndex) {
            this.steps[stepIndex].images.push({
                position: '',
                label: 'Select image',
                file: '',
                src: '',
            });
        },
        deleteImage(stepIndex, imageIndex) {
            this.steps[stepIndex].images.splice(imageIndex, 1)
        },
        // Files:
        addFile(stepIndex) {
            this.steps[stepIndex].files.push({
                name: '',
                label: 'Select file',
                file: '',
            });
        },
        deleteFile(stepIndex, fileIndex) {
            this.steps[stepIndex].files.splice(fileIndex, 1)
        },
        fileChange(event, type, stepIndex, imageIndex) {
            this.steps[stepIndex][type][imageIndex].label = event.target.files[0].name;
            this.steps[stepIndex][type][imageIndex].file = event.target.files[0];
            if (type == 'images' && event.target && event.target.files[0]) {
                this.steps[stepIndex][type][imageIndex].src = URL.createObjectURL(this.steps[stepIndex][type][imageIndex].file);
            }
        },
        // Links:
        addLink(stepIndex) {
            this.steps[stepIndex].links.push({
                label: 'Select link',
                src: '',
            });
        },
        deleteLink(stepIndex, linkIndex) {
            this.steps[stepIndex].links.splice(linkIndex, 1)
        },
        // Send data:
        submitGuide(event) {
            event.preventDefault();
            axios.post('http://localhost/post.php', {
                title: this.title,
                device: this.device,
                group: this.group,
                steps: this.steps,
                test: 'ok'
            })
                .then(function (response) {
                    alert(response.data);
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    }
});