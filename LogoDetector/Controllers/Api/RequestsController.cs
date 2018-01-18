using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using LogoDetector.Models;
using WebGrease.Extensions;

namespace LogoDetector.Controllers.Api
{
    public class RequestsController : ApiController
    {

        // Post /api/requests
        [HttpPost]
        public IHttpActionResult CreateRequest(DetectRequest request)
        {
            // set up process start info
            var startInfo = new ProcessStartInfo();
            startInfo.WorkingDirectory = System.Web.Hosting.HostingEnvironment.MapPath("~/Python");
            startInfo.FileName = "C:/Python27/python.exe";
            string cmd = "read_video.py";
            string args = "\"" + request.VidUrl + "\" ";
            foreach( string path in request.TemplateUrls )
            {
                string pathFormat = "\"" + path + "\" ";
                args += pathFormat;
            }
            startInfo.Arguments = string.Format("{0} {1}", cmd, args);

            // launch process
            Process process = Process.Start(startInfo);

            // wait for process exit
            process?.WaitForExit();

            return Ok();
        }
    }
}
