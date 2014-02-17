     $(document).ready(function(){
        var issue = /#[\d]+/; //#123
        var project = /@[a-z A-Z\-\d]+/; //@project
        var hs = /[\d\.]+hs?/; //12h o 12hs
        var activity = /\$[a-z A-Z\d]+/; //$dev
        var date = /!([\d])+\/([\d])/; //!3/3
        var projs, issues, activities;
        var arr = [];
        var kta = [0, 0, 0, 0, 0]
        window.cont = 0;

        var placeCaretAtEnd = function (el) {
            el.focus();
            if (typeof window.getSelection != "undefined"
                    && typeof document.createRange != "undefined") {
                var range = document.createRange();
                range.selectNodeContents(el);
                range.collapse(false);
                var sel = window.getSelection();
                sel.removeAllRanges();
                sel.addRange(range);
            } else if (typeof document.body.createTextRange != "undefined") {
                var textRange = document.body.createTextRange();
                textRange.moveToElementText(el);
                textRange.collapse(false);
                textRange.select();
            }
         }

         //experimental space

          $.getJSON('/entries/sendinfo', function(data) {
                projs = data[0];
                issues = data[1];
                activities = data[2];

                $.each(projs, function( index, value ) {
                    arr.push(value);
                });
                $.each(issues, function( index, value ) {
                    arr.push(value);
                });
                $.each(activities, function( index, value ) {
                    arr.push(value.replace('*', ''));
                    console.log(value);
                });
                $('#loading').css('display', 'none');
                $('#ent2').attr('contenteditable', 'true');
                $('#ent2').tagautocomplete({
                    source: arr,
                    character: '@#$', //accept both @ and #
                    after: function () {
                        $('#ent2').focus();
                        $('#ent2').append('\u200b\r');
                        placeCaretAtEnd($('#ent2').get(0));
                    } //to run after selection
                });
          });

        window.SetMenuPosition(250, -158);
         //end of this space

        var undecode = function(data){
            var values = [];

            var splitted = data.split('\n');
            for(var i = 0;i < splitted.length;i++){
                var line = splitted[i],
                issue_value = line.match(issue)[0],
                project_value = line.match(project)[0],
                hs_value = line.match(hs)[0],
                //activity_value = line.match(activity)[0],
                activity_value = 0,
                date_value = line.match(date)[0];
                line = line.replace(issue, '');
                line = line.replace(project, '');
                line = line.replace(hs, '');
                //line = line.replace(activity, '');
                line = line.replace(date_value, '');
                line = line.replace('   ', '');
                $.each(activities, function( index, value ) {
                    if (line.replace(value, '') != line){
                        activity_value = value;
                    }
                });
                line = line.replace(activity_value,'');
                console.log(hs_value);
                console.log(activity_value);
                console.log(project_value);
                console.log(issue_value);
                console.log(date_value);
                console.log(line);
                project_value = project_value.replace('@', '');
                issue_value = issue_value.replace('#', '');
                activity_value = activity_value.replace('$', '');
                values.push([project_value, issue_value, hs_value, line, activity_value, date_value]);
                console.log(values);
                //} //catch (e) {
                   // console.log('error');
                //}
            }
            return values;
        }
        function ParseDIVText(){
            var domString = "", temp = "";
            $("#ent2 div").each(function(){
                temp = $(this).html();
                domString += "<br>" + ((temp == "<br>") ? "" : temp);
            });

            alert(domString);
        }

        $('#ent2').keydown(function(e){
            console.log(e.which);
            if (e.which === 49 && e.shiftKey){
                e.preventDefault();
                if (cont != 0){cont -= 1;}
                //console.log('!');
                //$(this).trigger("EXCLAMATION_KEY");
                //e.preventDefault();
                $(this).datepicker({
                    dateFormat: 'dd/mm',
                    //showOn: "button",
                    maxDate: new Date(),
                    onSelect: function(){
                        var t1  = $(this).datepicker('getDate').getDate();
                        var t2 = $(this).datepicker('getDate').getMonth()+1;
                        $('.ui-datepicker-inline').datepicker().hide();
                        $('#ent2').append('<span class="label label-default">' + '!' + t1 + '/' + t2 + '</span>');
                        $('#ent2').focus();
                        placeCaretAtEnd($('#ent2').get(0));
                    }

               });
               $('.ui-datepicker-inline').attr('contenteditable', 'false');
               //console.log(t1);
               //e.preventDefault();
               $(".label-danger").text($(".label-danger").text().replace("!", ""));

               }
            else if (e.which === 50 && e.shiftKey){
                $("#ent2").append("\v\r")
                if (cont != 0){cont -= 1;}
                e.preventDefault();
                $('#ent2').append('<span class="label label-info">@</span>');
                $('#ent2').focus();
                placeCaretAtEnd($('#ent2').get(0));
            }
            else if (e.which === 51 && e.shiftKey){
                if (cont != 0){cont -= 1;}
                e.preventDefault();
                $('#ent2').append('<span class="label label-danger">#</span>');
                $('#ent2').focus();
                placeCaretAtEnd($('#ent2').get(0));
            }
            else if (e.which === 52 && e.shiftKey){
                if (cont != 0){cont -= 1;}
                e.preventDefault();
                $('#ent2').append('<span class="label label-primary">$</span>');
                $('#ent2').focus();
                placeCaretAtEnd($('#ent2').get(0));
            }
            else if (e.which === 8){
                $("#ent2 font").attr("color", "#000000");
                $("#ent2 font").attr("size", 2);
                $("#ent2 font span").css("background-color", "white");
            }
        });
        $('#ent2').keyup(function(e){
            if (e.keyCode == 13){
                $(this).trigger("ENTER_KEY");
            }
        });
        $('#ent2').bind("ENTER_KEY", function(e){
            $('ent2').remove('div');
            cont += 1;
            if (cont > 2){
            cont = 2;
            }
            $('#ent2').focus();
            console.log('Here');
            if (window.cont == 2){
                $('#ent2').focus();
                console.log("Cumplido");
                $('#ent2').append('\u200b\r\n');
                placeCaretAtEnd($('#ent2').get(0));
            }
        });
        $('#ent2').bind("EXCLAMATION_KEY", function(e){
            console.log("!test!");
            $(this).datepicker({
            dateFormat: 'dd/mm',
            //showOn: "button",
            maxDate: new Date(),
            onSelect: function(){
                var t1  = $(this).datepicker('getDate').getDate();
                var t2 = $(this).datepicker('getDate').getMonth()+1;
                $('.ui-datepicker-inline').datepicker().hide();
                $('#ent2').append('<span class="label label-default">' + '!' + t1 + '/' + t2 + '</span>');
                $('#ent2').focus();
                placeCaretAtEnd($('#ent2').get(0));
            }
            });
            $('.ui-datepicker-inline').attr('contenteditable', 'false');
            $(".label-danger").text($(".label-danger").text().replace("!", ""));
        });
	 });
