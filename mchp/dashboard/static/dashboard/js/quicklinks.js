$(document).ready(function() {
    openQuickLinks();
    var cols = document.querySelectorAll('#columns .column');
    [].forEach.call(cols, function(col) {
        col.addEventListener('dragstart', handleDragStart, false);
        col.addEventListener('dragenter', handleDragEnter, false);
        col.addEventListener('dragover', handleDragOver, false);
        col.addEventListener('dragleave', handleDragLeave, false);
        col.addEventListener('drop', handleDrop, false);
        col.addEventListener('dragend', handleDragEnd, false);
    });
    var dragSrcEl = null;

    function handleDragStart(e) {
        //this.style.opacity = '0.4';
        dragSrcEl = this;
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', this.innerHTML);
    }

    function handleDragOver(e) {
        this.classList.add('over');
        if (e.preventDefault) {
            e.preventDefault();
        }
        e.dataTransfer.dropEffect = 'move';
        return false;
    }

    function handleDragEnter(e) {
        this.classList.add('over');
    }

    function handleDragLeave(e) {
        this.classList.remove('over');
    }

    function handleDrop(e) {
        this.classList.remove('over');
        if (e.stopPropagation) {
            e.stopPropagation();
        }
        if (dragSrcEl != this) {
            dragSrcEl.innerHTML = this.innerHTML;
            this.innerHTML = e.dataTransfer.getData('text/html');
        }
        return false;
    }

    function handleDragEnd(e) {
        this.style.opacity = '1';
        [].forEach.call(cols, function(col) {
            col.classList.remove('over');
        });
    }
    var id = 0;
    // Trigger action when the contexmenu is about to be shown
    $(".column").bind("contextmenu", function(event) {
        id = $(this).attr('id');
        // Avoid the real one
        event.preventDefault();
        // Show contextmenu
        $(".custom-menu").toggle(100).
            // In the right position (the mouse)
        css({
            top: event.pageY - 10 + "px",
            left: event.pageX - 10 + "px"
        });
    });
    // If the document is clicked somewhere
    $(".custom-menu").bind("mouseleave", function() {
        $(".custom-menu").hide(100);
    });
    $(".custom-menu div").click(function() {
        // This is the triggered action name
        switch ($(this).attr("data-action")) {
            // A case for each action. Should personalize to your actions
            case "edit":
                break;
            case "delete":
                deleteLink(id);
                $(".custom-menu").hide();
                $('#' + id).hide('100', function() {
                    $('#' + id).remove();
                });
                break;
        }
    });
    // Edit box js
    var dialog, form,
        urlRegex = /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/,
        name = $("#name"),
        url = $("#url"),
        allFields = $([]).add(name).add(url),
        tips = $(".validateTips");

    function updateTips(t) {
        tips.text(t).addClass("ui-state-highlight");
        setTimeout(function() {
            tips.removeClass("ui-state-highlight", 1500);
        }, 500);
    }

    function checkLength(o, n, min, max) {
        if (o.val().length > max || o.val().length < min) {
            o.addClass("ui-state-error");
            updateTips("Length of " + n + " must be between " + min + " and " + max + ".");
            return false;
        } else {
            return true;
        }
    }

    function checkRegexp(o, regexp, n) {
        if (!(regexp.test(o.val()))) {
            o.addClass("ui-state-error");
            updateTips(n);
            return false;
        } else {
            return true;
        }
    }

    function addLink() {
        console.log("addlink");
        var valid = true;
        allFields.removeClass("ui-state-error");
        valid = valid && checkLength(name, "link", 1, 16);
        valid = valid && checkLength(url, "url", 6, 80);
        valid = valid && checkRegexp(name, /^[ -~]/i, "Quicklink name may contain any characters");
        valid = valid && checkRegexp(url, urlRegex, "eg. mycollegehomepage.com");
        if (valid) {
            $('#' + id).children("a").text(name.val());
            $('#' + id).children("a").attr("href", url.val());
            dialog.dialog("close");
        }
        return valid;
    }

    function openQuickLinks() {
        if (localStorage.length == 0) {
            // Get quicklinks from school and add to localStorage
            // Get quicklinks from user and add to localStorage
        } else {
            for (var i = 0; i < localStorage.length; i++) {
                createLink(JSON.parse(localStorage.getItem(localStorage.key(i))));
            }
        }
    }

    function createLink(data) {
        if (data == undefined) data = {
            id: +new Date(),
            text: "",
            url: ""
        };
        id = data.id;
        var link = "<li id=\"" + data.id + "\" class=\"column\"><a href=\"" + data.url + "\">" + data.text + "</a></li>"
        $("#columns").append(link);
        $("#addLink").insertAfter($('#' + id));
    }

    function saveLink() {
        console.log("saveLink");
        link = $('#' + id);
        obj = {
            id: link.attr("id"),
            text: link.children().text(),
            url: link.children().attr("href")
        }
        localStorage.setItem("link-" + obj.id, JSON.stringify(obj));
    }

    function deleteLink(id) {
        localStorage.removeItem("link-" + id);
    }
    dialog = $("#dialog-form").dialog({
        autoOpen: false,
        height: 400,
        width: 350,
        modal: true,
        buttons: {
            "Save": function() {
                addLink();
                saveLink();
            },
            Cancel: function() {
                if ($('#' + id).text() == "") $('#' + id).remove();
                dialog.dialog("close");
            }
        },
        close: function() {
            if ($('#' + id).text() == "") $('#' + id).remove();
            form[0].reset();
            allFields.removeClass("ui-state-error");
        }
    });
    form = dialog.find("form").on("submit", function(event) {
        event.preventDefault();
        addLink();
    });
    $("#edit").on("click", function() {
        $(".custom-menu").hide(100);
        dialog.dialog("open");
    });
    $("#addLink").on("click", function() {
        createLink();
        dialog.dialog("open");
    });
});
