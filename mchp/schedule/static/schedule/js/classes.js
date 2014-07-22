/*
 * classes.js
 *
 * This file handles the trigger of user pop-ups.
 */
$(function() {
	//trigger friends pop-up on hover and stay
	$(".friend-popover").popover ({ 
		trigger: "manual",
		html: true,
		content : '<div class="text-center" style="width:200px;"><img class="img-circle img-thumbnail" src="https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xfp1/t1.0-1/p160x160/1948074_10151938632961930_1503647379_n.jpg" width="120px"/><h5 style="margin-bottom:0px;">Mitch Kessler</h5><small style="margin-bottom:0px;">@mitchellias</small><h5><small>20 friends and 3 classes in common</small></h5><hr><small><div class="progress" style="margin-bottom:;"><a href="#" class="progress-bar progress-bar-success" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-primary" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-info" style="width:60%;" ></a></div></small></div>'
		
	})

    .on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    })
    .on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide")
            }
        }, 100);
    });
    //trigger non-friend pop-up on hover and stay
	$(".classmate-popover").popover ({ 
		trigger: "manual",
		html: true,
		content : '<div class="text-center" style="width:200px;"><img class="img-circle img-thumbnail" src="https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpa1/v/t1.0-1/c0.0.160.160/p160x160/10517552_10152650070421654_3530025072014623093_n.jpg?oh=f5058fe314e993257083689be59e1562&oe=54452C8D&__gda__=1412673103_2cf0341e968f31bbb25b05304d3b47eb" width="120px"/><h5>Mike</h5><h5><small>20 friends and 3 classes in common</small></h5><p class="small"><button class="btn btn-primary btn-xs btn-block">Friend Mike</button></p><small><hr><div class="progress" style="margin-bottom:;"><a href="#" class="progress-bar progress-bar-success" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-primary" style="width:20%;"></a><a href="#" class="progress-bar progress-bar-info" style="width:60%;" ></a></div></small></div>'
		
	})

    .on("mouseenter", function () {
        var _this = this;
        $(this).popover("show");
        $(".popover").on("mouseleave", function () {
            $(_this).popover('hide');
        });
    })
    .on("mouseleave", function () {
        var _this = this;
        setTimeout(function () {
            if (!$(".popover:hover").length) {
                $(_this).popover("hide")
            }
        }, 100);
    });
});
