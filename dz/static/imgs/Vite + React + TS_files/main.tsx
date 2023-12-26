import __vite__cjsImport0_react_jsxDevRuntime from "/gp_frontend/node_modules/.vite/deps/react_jsx-dev-runtime.js?v=a482de23"; const jsxDEV = __vite__cjsImport0_react_jsxDevRuntime["jsxDEV"];
import { BrowserRouter, Route, Routes, Navigate } from "/gp_frontend/node_modules/.vite/deps/react-router-dom.js?v=a482de23";
import OperationPage from "/gp_frontend/src/page/OperationPage/OperationPage.tsx";
import __vite__cjsImport3_reactDom_client from "/gp_frontend/node_modules/.vite/deps/react-dom_client.js?v=a482de23"; const ReactDOM = __vite__cjsImport3_reactDom_client.__esModule ? __vite__cjsImport3_reactDom_client.default : __vite__cjsImport3_reactDom_client;
import { Provider } from "/gp_frontend/node_modules/.vite/deps/react-redux.js?v=a482de23";
import store from "/gp_frontend/src/slices/store.ts";
import { QueryClient, QueryClientProvider } from "/gp_frontend/node_modules/.vite/deps/react-query.js?v=a482de23";
const root = ReactDOM.createRoot(
  document.getElementById("myroot")
);
const queryClient = new QueryClient();
root.render(
  /* @__PURE__ */ jsxDEV(QueryClientProvider, { client: queryClient, children: /* @__PURE__ */ jsxDEV(Provider, { store, children: /* @__PURE__ */ jsxDEV(BrowserRouter, { children: /* @__PURE__ */ jsxDEV("div", { className: "content-wrapper", children: /* @__PURE__ */ jsxDEV(Routes, { children: [
    /* @__PURE__ */ jsxDEV(Route, { path: "/", element: /* @__PURE__ */ jsxDEV(Navigate, { to: "/operaiton", replace: true }, void 0, false, {
      fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
      lineNumber: 49,
      columnNumber: 50
    }, this) }, void 0, false, {
      fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
      lineNumber: 49,
      columnNumber: 25
    }, this),
    /* @__PURE__ */ jsxDEV(Route, { path: "operations/:id", element: /* @__PURE__ */ jsxDEV(OperationPage, {}, void 0, false, {
      fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
      lineNumber: 51,
      columnNumber: 63
    }, this) }, void 0, false, {
      fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
      lineNumber: 51,
      columnNumber: 25
    }, this)
  ] }, void 0, true, {
    fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
    lineNumber: 48,
    columnNumber: 21
  }, this) }, void 0, false, {
    fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
    lineNumber: 46,
    columnNumber: 17
  }, this) }, void 0, false, {
    fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
    lineNumber: 42,
    columnNumber: 13
  }, this) }, void 0, false, {
    fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
    lineNumber: 40,
    columnNumber: 9
  }, this) }, void 0, false, {
    fileName: "/home/alla/rip_front/rip_front/src/main.tsx",
    lineNumber: 38,
    columnNumber: 3
  }, this)
);

//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJtYXBwaW5ncyI6IkFBZ0RpRDtBQXJDakQsU0FBUUEsZUFBZUMsT0FBT0MsUUFBUUMsZ0JBQWU7QUFFckQsT0FBT0MsbUJBQW1CO0FBRTFCLE9BQU9DLGNBQWM7QUFFckIsU0FBU0MsZ0JBQWdCO0FBQ3pCLE9BQU9DLFdBQVc7QUFLbEIsU0FBUUMsYUFBYUMsMkJBQTBCO0FBRy9DLE1BQU1DLE9BQU9MLFNBQVNNO0FBQUFBLEVBQ2xCQyxTQUFTQyxlQUFlLFFBQVE7QUFDcEM7QUFFQSxNQUFNQyxjQUFjLElBQUlOLFlBQVk7QUFNcENFLEtBQUtLO0FBQUFBLEVBQ0QsdUJBQUMsdUJBQW9CLFFBQVFELGFBRXpCLGlDQUFDLFlBQVMsT0FFTixpQ0FBQyxpQkFJRyxpQ0FBQyxTQUFJLFdBQVUsbUJBRVgsaUNBQUMsVUFDRztBQUFBLDJCQUFDLFNBQU0sTUFBSyxLQUFJLFNBQVMsdUJBQUMsWUFBUyxJQUFHLGNBQWEsU0FBTyxRQUFqQztBQUFBO0FBQUE7QUFBQTtBQUFBLFdBQWlDLEtBQTFEO0FBQUE7QUFBQTtBQUFBO0FBQUEsV0FBOEQ7QUFBQSxJQUU5RCx1QkFBQyxTQUFNLE1BQUssa0JBQWlCLFNBQVMsdUJBQUMsbUJBQUQ7QUFBQTtBQUFBO0FBQUE7QUFBQSxXQUFjLEtBQXBEO0FBQUE7QUFBQTtBQUFBO0FBQUEsV0FBdUQ7QUFBQSxPQUgzRDtBQUFBO0FBQUE7QUFBQTtBQUFBLFNBS0EsS0FQSjtBQUFBO0FBQUE7QUFBQTtBQUFBLFNBU0EsS0FiSjtBQUFBO0FBQUE7QUFBQTtBQUFBLFNBZUosS0FqQkE7QUFBQTtBQUFBO0FBQUE7QUFBQSxTQW1CQSxLQXJCSjtBQUFBO0FBQUE7QUFBQTtBQUFBLFNBdUJBO0FBQ0oiLCJuYW1lcyI6WyJCcm93c2VyUm91dGVyIiwiUm91dGUiLCJSb3V0ZXMiLCJOYXZpZ2F0ZSIsIk9wZXJhdGlvblBhZ2UiLCJSZWFjdERPTSIsIlByb3ZpZGVyIiwic3RvcmUiLCJRdWVyeUNsaWVudCIsIlF1ZXJ5Q2xpZW50UHJvdmlkZXIiLCJyb290IiwiY3JlYXRlUm9vdCIsImRvY3VtZW50IiwiZ2V0RWxlbWVudEJ5SWQiLCJxdWVyeUNsaWVudCIsInJlbmRlciJdLCJzb3VyY2VzIjpbIm1haW4udHN4Il0sInNvdXJjZXNDb250ZW50IjpbIi8qaW1wb3J0IFJlYWN0IGZyb20gJ3JlYWN0J1xuaW1wb3J0IFJlYWN0RE9NIGZyb20gJ3JlYWN0LWRvbS9jbGllbnQnXG5pbXBvcnQgQXBwIGZyb20gJy4vQXBwLnRzeCdcbmltcG9ydCAnLi9pbmRleC5jc3MnXG4vL2ltcG9ydCAnYm9vdHN0cmFwL2Rpc3QvY3NzL2Jvb3RzdHJhcC5taW4uY3NzJ1xuUmVhY3RET00uY3JlYXRlUm9vdChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnbXlyb290JykhKS5yZW5kZXIoXG4gIDxSZWFjdC5TdHJpY3RNb2RlPlxuICAgIDxBcHAgLz5cbiAgPC9SZWFjdC5TdHJpY3RNb2RlPixcbilcbiovXG5pbXBvcnQge0Jyb3dzZXJSb3V0ZXIsIFJvdXRlLCBSb3V0ZXMsIE5hdmlnYXRlfSBmcm9tIFwicmVhY3Qtcm91dGVyLWRvbVwiO1xuLy9pbXBvcnQgT3BlcmF0aW9ucyBmcm9tIFwiLi9wYWdlcy9PcGVyYXRpb25zUGFnZS9PcGVyYXRpb25zUGFnZS50c3hcIjtcbmltcG9ydCBPcGVyYXRpb25QYWdlIGZyb20gXCIuL3BhZ2UvT3BlcmF0aW9uUGFnZS9PcGVyYXRpb25QYWdlLnRzeFwiXG4vL2ltcG9ydCBCcmVhY2hlcyBmcm9tIFwiLi9wYWdlcy9CcmVhY2hlc1BhZ2UvQnJlYWNoZXNQYWdlLnRzeFwiO1xuaW1wb3J0IFJlYWN0RE9NIGZyb20gXCJyZWFjdC1kb20vY2xpZW50XCI7XG4vL2ltcG9ydCBMb2dpblBhZ2UgZnJvbSBcIi4vcGFnZXMvTG9naW5QYWdlL0xvZ2luUGFnZS50c3hcIjtcbmltcG9ydCB7IFByb3ZpZGVyIH0gZnJvbSBcInJlYWN0LXJlZHV4XCI7XG5pbXBvcnQgc3RvcmUgZnJvbSBcIi4vc2xpY2VzL3N0b3JlLnRzXCI7XG4vL2ltcG9ydCBQcm9maWxlUGFnZSBmcm9tIFwiLi9wYWdlcy9Qcm9maWxlUGFnZS9Qcm9maWxlUGFnZS50c3hcIjtcbi8vaW1wb3J0IE5hdmJhciBmcm9tIFwiLi9jb21wb25lbnRzL05hdmJhci9OYXZiYXIudHN4XCI7XG4vL2ltcG9ydCBcIi4vc3R5bGVzL3N0eWxlcy5zY3NzXCJcbi8vaW1wb3J0IEJyZWFjaFBhZ2UgZnJvbSBcIi4vcGFnZXMvQnJlYWNoUGFnZS9CcmVhY2hQYWdlXCI7XG5pbXBvcnQge1F1ZXJ5Q2xpZW50LCBRdWVyeUNsaWVudFByb3ZpZGVyfSBmcm9tIFwicmVhY3QtcXVlcnlcIjtcbi8vaW1wb3J0IEJyZWFkY3J1bWJzIGZyb20gXCIuL2NvbXBvbmVudHMvQnJlYWRjcnVtYnMvQnJlYWRjcnVtYnNcIjtcblxuY29uc3Qgcm9vdCA9IFJlYWN0RE9NLmNyZWF0ZVJvb3QoXG4gICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ215cm9vdCcpIGFzIEhUTUxFbGVtZW50XG4pO1xuXG5jb25zdCBxdWVyeUNsaWVudCA9IG5ldyBRdWVyeUNsaWVudCgpXG4vKjxSb3V0ZSBwYXRoPVwiZmluZXMvXCIgZWxlbWVudD17PE9wZXJhdGlvbnMvPn0vPlxuICAgICAgICAgICAgICAgICAgICAgICAgPFJvdXRlIHBhdGg9XCJicmVhY2hlcy9cIiBlbGVtZW50PXs8QnJlYWNoZXMvPn0vPlxuICAgICAgICAgICAgICAgICAgICAgICAgPFJvdXRlIHBhdGg9XCJicmVhY2hlcy9kcmFmdC9cIiBlbGVtZW50PXs8QnJlYWNoUGFnZS8+fS8+XG4gICAgICAgICAgICAgICAgICAgICAgICA8Um91dGUgcGF0aD1cImxvZ2luL1wiIGVsZW1lbnQ9ezxMb2dpblBhZ2UvPn0vPlxuICAgICAgICAgICAgICAgICAgICAgICAgPFJvdXRlIHBhdGg9XCJwcm9maWxlL1wiIGVsZW1lbnQ9ezxQcm9maWxlUGFnZS8+fS8+ICovXG5yb290LnJlbmRlcihcbiAgICA8UXVlcnlDbGllbnRQcm92aWRlciBjbGllbnQ9e3F1ZXJ5Q2xpZW50fT5cblxuICAgICAgICA8UHJvdmlkZXIgc3RvcmU9e3N0b3JlfT5cblxuICAgICAgICAgICAgPEJyb3dzZXJSb3V0ZXI+XG5cbiAgICAgICAgICAgICAgICBcblxuICAgICAgICAgICAgICAgIDxkaXYgY2xhc3NOYW1lPVwiY29udGVudC13cmFwcGVyXCI+XG5cbiAgICAgICAgICAgICAgICAgICAgPFJvdXRlcz5cbiAgICAgICAgICAgICAgICAgICAgICAgIDxSb3V0ZSBwYXRoPVwiL1wiIGVsZW1lbnQ9ezxOYXZpZ2F0ZSB0bz1cIi9vcGVyYWl0b25cIiByZXBsYWNlIC8+fSAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgICAgICAgICAgICAgICAgICAgICA8Um91dGUgcGF0aD1cIm9wZXJhdGlvbnMvOmlkXCIgZWxlbWVudD17PE9wZXJhdGlvblBhZ2UvPn0vPlxuICAgICAgICAgICAgICAgICAgICAgICAgXG4gICAgICAgICAgICAgICAgICAgIDwvUm91dGVzPlxuXG4gICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgICAgXG4gICAgICAgIDwvQnJvd3NlclJvdXRlcj5cblxuICAgICAgICA8L1Byb3ZpZGVyPlxuXG4gICAgPC9RdWVyeUNsaWVudFByb3ZpZGVyPlxuKTsiXSwiZmlsZSI6Ii9ob21lL2FsbGEvcmlwX2Zyb250L3JpcF9mcm9udC9zcmMvbWFpbi50c3gifQ==