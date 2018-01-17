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
            string cmd = "py \"" + System.Web.Hosting.HostingEnvironment.MapPath("~/Python/read_video.py") + "\"";

            var startInfo = new ProcessStartInfo();
            startInfo.WorkingDirectory = System.Web.Hosting.HostingEnvironment.MapPath("~/Python");
            startInfo.FileName = "read_video.py";
            startInfo.Arguments = request.VidUrl;

            Process process = Process.Start(startInfo);

            process?.WaitForExit();

            return Ok();
        }
    }
}
